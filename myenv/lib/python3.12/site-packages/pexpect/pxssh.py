'''This class extends pexpect.spawn to specialize setting up SSH connections.
This adds methods for login, logout, and expecting the shell prompt.

PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2012, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

'''

from pexpect import ExceptionPexpect, TIMEOUT, EOF, spawn
import time
import os
import sys
import re

__all__ = ['ExceptionPxssh', 'pxssh']

# Exception classes used by this module.
class ExceptionPxssh(ExceptionPexpect):
    '''Raised for pxssh exceptions.
    '''

if sys.version_info > (3, 0):
    from shlex import quote
else:
    _find_unsafe = re.compile(r'[^\w@%+=:,./-]').search

    def quote(s):
        """Return a shell-escaped version of the string *s*."""
        if not s:
            return "''"
        if _find_unsafe(s) is None:
            return s

        # use single quotes, and put single quotes into double quotes
        # the string $'b is then quoted as '$'"'"'b'
        return "'" + s.replace("'", "'\"'\"'") + "'"

class pxssh (spawn):
    '''This class extends pexpect.spawn to specialize setting up SSH
    connections. This adds methods for login, logout, and expecting the shell
    prompt. It does various tricky things to handle many situations in the SSH
    login process. For example, if the session is your first login, then pxssh
    automatically accepts the remote certificate; or if you have public key
    authentication setup then pxssh won't wait for the password prompt.

    pxssh uses the shell prompt to synchronize output from the remote host. In
    order to make this more robust it sets the shell prompt to something more
    unique than just $ or #. This should work on most Borne/Bash or Csh style
    shells.

    Example that runs a few commands on a remote server and prints the result::

        from pexpect import pxssh
        import getpass
        try:
            s = pxssh.pxssh()
            hostname = raw_input('hostname: ')
            username = raw_input('username: ')
            password = getpass.getpass('password: ')
            s.login(hostname, username, password)
            s.sendline('uptime')   # run a command
            s.prompt()             # match the prompt
            print(s.before)        # print everything before the prompt.
            s.sendline('ls -l')
            s.prompt()
            print(s.before)
            s.sendline('df')
            s.prompt()
            print(s.before)
            s.logout()
        except pxssh.ExceptionPxssh as e:
            print("pxssh failed on login.")
            print(e)

    Example showing how to specify SSH options::

        from pexpect import pxssh
        s = pxssh.pxssh(options={
                            "StrictHostKeyChecking": "no",
                            "UserKnownHostsFile": "/dev/null"})
        ...

    Note that if you have ssh-agent running while doing development with pxssh
    then this can lead to a lot of confusion. Many X display managers (xdm,
    gdm, kdm, etc.) will automatically start a GUI agent. You may see a GUI
    dialog box popup asking for a password during development. You should turn
    off any key agents during testing. The 'force_password' attribute will turn
    off public key authentication. This will only work if the remote SSH server
    is configured to allow password logins. Example of using 'force_password'
    attribute::

            s = pxssh.pxssh()
            s.force_password = True
            hostname = raw_input('hostname: ')
            username = raw_input('username: ')
            password = getpass.getpass('password: ')
            s.login (hostname, username, password)

    `debug_command_string` is only for the test suite to confirm that the string
    generated for SSH is correct, using this will not allow you to do
    anything other than get a string back from `pxssh.pxssh.login()`.
    '''

    def __init__ (self, timeout=30, maxread=2000, searchwindowsize=None,
                    logfile=None, cwd=None, env=None, ignore_sighup=True, echo=True,
                    options={}, encoding=None, codec_errors='strict',
                    debug_command_string=False, use_poll=False):

        spawn.__init__(self, None, timeout=timeout, maxread=maxread,
                       searchwindowsize=searchwindowsize, logfile=logfile,
                       cwd=cwd, env=env, ignore_sighup=ignore_sighup, echo=echo,
                       encoding=encoding, codec_errors=codec_errors, use_poll=use_poll)

        self.name = '<pxssh>'

        #SUBTLE HACK ALERT! Note that the command that SETS the prompt uses a
        #slightly different string than the regular expression to match it. This
        #is because when you set the prompt the command will echo back, but we
        #don't want to match the echoed command. So if we make the set command
        #slightly different than the regex we eliminate the problem. To make the
        #set command different we add a backslash in front of $. The $ doesn't
        #need to be escaped, but it doesn't hurt and serves to make the set
        #prompt command different than the regex.

        # used to match the command-line prompt
        self.UNIQUE_PROMPT = r"\[PEXPECT\][\$\#] "
        self.PROMPT = self.UNIQUE_PROMPT

        # used to set shell command-line prompt to UNIQUE_PROMPT.
        self.PROMPT_SET_SH = r"PS1='[PEXPECT]\$ '"
        self.PROMPT_SET_CSH = r"set prompt='[PEXPECT]\$ '"
        self.PROMPT_SET_ZSH = "prompt restore;\nPS1='[PEXPECT]%(!.#.$) '"
        self.SSH_OPTS = (" -o 'PubkeyAuthentication=no'")
# Disabling host key checking, makes you vulnerable to MITM attacks.
#                + " -o 'StrictHostKeyChecking=no'"
#                + " -o 'UserKnownHostsFile /dev/null' ")
        # Disabling X11 forwarding gets rid of the annoying SSH_ASKPASS from
        # displaying a GUI password dialog. I have not figured out how to
        # disable only SSH_ASKPASS without also disabling X11 forwarding.
        # Unsetting SSH_ASKPASS on the remote side doesn't disable it! Annoying!
        #self.SSH_OPTS = "-x -o 'PubkeyAuthentication=no'"
        self.force_password = False

        self.debug_command_string = debug_command_string

        # User defined SSH options, eg,
        # ssh.otions = dict(StrictHostKeyChecking="no",UserKnownHostsFile="/dev/null")
        self.options = options

    def levenshtein_distance(self, a, b):
        '''This calculates the Levenshtein distance between a and b.
        '''

        n, m = len(a), len(b)
        if n > m:
            a,b = b,a
            n,m = m,n
        current = range(n+1)
        for i in range(1,m+1):
            previous, current = current, [i]+[0]*n
            for j in range(1,n+1):
                add, delete = previous[j]+1, current[j-1]+1
                change = previous[j-1]
                if a[j-1] != b[i-1]:
                    change = change + 1
                current[j] = min(add, delete, change)
        return current[n]

    def try_read_prompt(self, timeout_multiplier):
        '''This facilitates using communication timeouts to perform
        synchronization as quickly as possible, while supporting high latency
        connections with a tunable worst case performance. Fast connections
        should be read almost immediately. Worst case performance for this
        method is timeout_multiplier * 3 seconds.
        '''

        # maximum time allowed to read the first response
        first_char_timeout = timeout_multiplier * 0.5

        # maximum time allowed between subsequent characters
        inter_char_timeout = timeout_multiplier * 0.1

        # maximum time for reading the entire prompt
        total_timeout = timeout_multiplier * 3.0

        prompt = self.string_type()
        begin = time.time()
        expired = 0.0
        timeout = first_char_timeout

        while expired < total_timeout:
            try:
                prompt += self.read_nonblocking(size=1, timeout=timeout)
                expired = time.time() - begin # updated total time expired
                timeout = inter_char_timeout
            except TIMEOUT:
                break

        return prompt

    def sync_original_prompt (self, sync_multiplier=1.0):
        '''This attempts to find the prompt. Basically, press enter and record
        the response; press enter again and record the response; if the two
        responses are similar then assume we are at the original prompt.
        This can be a slow function. Worst case with the default sync_multiplier
        can take 12 seconds. Low latency connections are more likely to fail
        with a low sync_multiplier. Best case sync time gets worse with a
        high sync multiplier (500 ms with default). '''

        # All of these timing pace values are magic.
        # I came up with these based on what seemed reliable for
        # connecting to a heavily loaded machine I have.
        self.sendline()
        time.sleep(0.1)

        try:
            # Clear the buffer before getting the prompt.
            self.try_read_prompt(sync_multiplier)
        except TIMEOUT:
            pass

        self.sendline()
        x = self.try_read_prompt(sync_multiplier)

        self.sendline()
        a = self.try_read_prompt(sync_multiplier)

        self.sendline()
        b = self.try_read_prompt(sync_multiplier)

        ld = self.levenshtein_distance(a,b)
        len_a = len(a)
        if len_a == 0:
            return False
        if float(ld)/len_a < 0.4:
            return True
        return False

    ### TODO: This is getting messy and I'm pretty sure this isn't perfect.
    ### TODO: I need to draw a flow chart for this.
    ### TODO: Unit tests for SSH tunnels, remote SSH command exec, disabling original prompt sync
    def login (self, server, username=None, password='', terminal_type='ansi',
                original_prompt=r"[#$]", login_timeout=10, port=None,
                auto_prompt_reset=True, ssh_key=None, quiet=True,
                sync_multiplier=1, check_local_ip=True,
                password_regex=r'(?i)(?:password:)|(?:passphrase for key)',
                ssh_tunnels={}, spawn_local_ssh=True,
                sync_original_prompt=True, ssh_config=None, cmd='ssh'):
        '''This logs the user into the given server.

        It uses 'original_prompt' to try to find the prompt right after login.
        When it finds the prompt it immediately tries to reset the prompt to
        something more easily matched. The default 'original_prompt' is very
        optimistic and is easily fooled. It's more reliable to try to match the original
        prompt as exactly as possible to prevent false matches by server
        strings such as the "Message Of The Day". On many systems you can
        disable the MOTD on the remote server by creating a zero-length file
        called :file:`~/.hushlogin` on the remote server. If a prompt cannot be found
        then this will not necessarily cause the login to fail. In the case of
        a timeout when looking for the prompt we assume that the original
        prompt was so weird that we could not match it, so we use a few tricks
        to guess when we have reached the prompt. Then we hope for the best and
        blindly try to reset the prompt to something more unique. If that fails
        then login() raises an :class:`ExceptionPxssh` exception.

        In some situations it is not possible or desirable to reset the
        original prompt. In this case, pass ``auto_prompt_reset=False`` to
        inhibit setting the prompt to the UNIQUE_PROMPT. Remember that pxssh
        uses a unique prompt in the :meth:`prompt` method. If the original prompt is
        not reset then this will disable the :meth:`prompt` method unless you
        manually set the :attr:`PROMPT` attribute.

        Set ``password_regex`` if there is a MOTD message with `password` in it.
        Changing this is like playing in traffic, don't (p)expect it to match straight
        away.

        If you require to connect to another SSH server from the your original SSH
        connection set ``spawn_local_ssh`` to `False` and this will use your current
        session to do so. Setting this option to `False` and not having an active session
        will trigger an error.

        Set ``ssh_key`` to a file path to an SSH private key to use that SSH key
        for the session authentication.
        Set ``ssh_key`` to `True` to force passing the current SSH authentication socket
        to the desired ``hostname``.

        Set ``ssh_config`` to a file path string of an SSH client config file to pass that
        file to the client to handle itself. You may set any options you wish in here, however
        doing so will require you to post extra information that you may not want to if you
        run into issues.

        Alter the ``cmd`` to change the ssh client used, or to prepend it with network
        namespaces. For example ```cmd="ip netns exec vlan2 ssh"``` to execute the ssh in
        network namespace named ```vlan```.
        '''

        session_regex_array = ["(?i)are you sure you want to continue connecting", original_prompt, password_regex, "(?i)permission denied", "(?i)terminal type", TIMEOUT]
        session_init_regex_array = []
        session_init_regex_array.extend(session_regex_array)
        session_init_regex_array.extend(["(?i)connection closed by remote host", EOF])

        ssh_options = ''.join([" -o '%s=%s'" % (o, v) for (o, v) in self.options.items()])
        if quiet:
            ssh_options = ssh_options + ' -q'
        if not check_local_ip:
            ssh_options = ssh_options + " -o'NoHostAuthenticationForLocalhost=yes'"
        if self.force_password:
            ssh_options = ssh_options + ' ' + self.SSH_OPTS
        if ssh_config is not None:
            if spawn_local_ssh and not os.path.isfile(ssh_config):
                raise ExceptionPxssh('SSH config does not exist or is not a file.')
            ssh_options = ssh_options + ' -F ' + ssh_config
        if port is not None:
            ssh_options = ssh_options + ' -p %s'%(str(port))
        if ssh_key is not None:
            # Allow forwarding our SSH key to the current session
            if ssh_key==True:
                ssh_options = ssh_options + ' -A'
            else:
                if spawn_local_ssh and not os.path.isfile(ssh_key):
                    raise ExceptionPxssh('private ssh key does not exist or is not a file.')
                ssh_options = ssh_options + ' -i %s' % (ssh_key)

        # SSH tunnels, make sure you know what you're putting into the lists
        # under each heading. Do not expect these to open 100% of the time,
        # The port you're requesting might be bound.
        #
        # The structure should be like this:
        # { 'local': ['2424:localhost:22'],  # Local SSH tunnels
        # 'remote': ['2525:localhost:22'],   # Remote SSH tunnels
        # 'dynamic': [8888] } # Dynamic/SOCKS tunnels
        if ssh_tunnels!={} and isinstance({},type(ssh_tunnels)):
            tunnel_types = {
                'local':'L',
                'remote':'R',
                'dynamic':'D'
            }
            for tunnel_type in tunnel_types:
                cmd_type = tunnel_types[tunnel_type]
                if tunnel_type in ssh_tunnels:
                    tunnels = ssh_tunnels[tunnel_type]
                    for tunnel in tunnels:
                        if spawn_local_ssh==False:
                            tunnel = quote(str(tunnel))
                        ssh_options = ssh_options + ' -' + cmd_type + ' ' + str(tunnel)

        if username is not None:
            ssh_options = ssh_options + ' -l ' + username
        elif ssh_config is None:
            raise TypeError('login() needs either a username or an ssh_config')
        else:  # make sure ssh_config has an entry for the server with a username
            with open(ssh_config, 'rt') as f:
                lines = [l.strip() for l in f.readlines()]

            server_regex = r'^Host\s+%s\s*$' % server
            user_regex = r'^User\s+\w+\s*$'
            config_has_server = False
            server_has_username = False
            for line in lines:
                if not config_has_server and re.match(server_regex, line, re.IGNORECASE):
                    config_has_server = True
                elif config_has_server and 'hostname' in line.lower():
                    pass
                elif config_has_server and 'host' in line.lower():
                    server_has_username = False  # insurance
                    break  # we have left the relevant section
                elif config_has_server and re.match(user_regex, line, re.IGNORECASE):
                    server_has_username = True
                    break

            if lines:
                del line

            del lines

            if not config_has_server:
                raise TypeError('login() ssh_config has no Host entry for %s' % server)
            elif not server_has_username:
                raise TypeError('login() ssh_config has no user entry for %s' % server)

        cmd += " %s %s" % (ssh_options, server)
        if self.debug_command_string:
            return(cmd)

        # Are we asking for a local ssh command or to spawn one in another session?
        if spawn_local_ssh:
            spawn._spawn(self, cmd)
        else:
            self.sendline(cmd)

        # This does not distinguish between a remote server 'password' prompt
        # and a local ssh 'passphrase' prompt (for unlocking a private key).
        i = self.expect(session_init_regex_array, timeout=login_timeout)

        # First phase
        if i==0:
            # New certificate -- always accept it.
            # This is what you get if SSH does not have the remote host's
            # public key stored in the 'known_hosts' cache.
            self.sendline("yes")
            i = self.expect(session_regex_array)
        if i==2: # password or passphrase
            self.sendline(password)
            i = self.expect(session_regex_array)
        if i==4:
            self.sendline(terminal_type)
            i = self.expect(session_regex_array)
        if i==7:
            self.close()
            raise ExceptionPxssh('Could not establish connection to host')

        # Second phase
        if i==0:
            # This is weird. This should not happen twice in a row.
            self.close()
            raise ExceptionPxssh('Weird error. Got "are you sure" prompt twice.')
        elif i==1: # can occur if you have a public key pair set to authenticate.
            ### TODO: May NOT be OK if expect() got tricked and matched a false prompt.
            pass
        elif i==2: # password prompt again
            # For incorrect passwords, some ssh servers will
            # ask for the password again, others return 'denied' right away.
            # If we get the password prompt again then this means
            # we didn't get the password right the first time.
            self.close()
            raise ExceptionPxssh('password refused')
        elif i==3: # permission denied -- password was bad.
            self.close()
            raise ExceptionPxssh('permission denied')
        elif i==4: # terminal type again? WTF?
            self.close()
            raise ExceptionPxssh('Weird error. Got "terminal type" prompt twice.')
        elif i==5: # Timeout
            #This is tricky... I presume that we are at the command-line prompt.
            #It may be that the shell prompt was so weird that we couldn't match
            #it. Or it may be that we couldn't log in for some other reason. I
            #can't be sure, but it's safe to guess that we did login because if
            #I presume wrong and we are not logged in then this should be caught
            #later when I try to set the shell prompt.
            pass
        elif i==6: # Connection closed by remote host
            self.close()
            raise ExceptionPxssh('connection closed')
        else: # Unexpected
            self.close()
            raise ExceptionPxssh('unexpected login response')
        if sync_original_prompt:
            if not self.sync_original_prompt(sync_multiplier):
                self.close()
                raise ExceptionPxssh('could not synchronize with original prompt')
        # We appear to be in.
        # set shell prompt to something unique.
        if auto_prompt_reset:
            if not self.set_unique_prompt():
                self.close()
                raise ExceptionPxssh('could not set shell prompt '
                                     '(received: %r, expected: %r).' % (
                                         self.before, self.PROMPT,))
        return True

    def logout (self):
        '''Sends exit to the remote shell.

        If there are stopped jobs then this automatically sends exit twice.
        '''
        self.sendline("exit")
        index = self.expect([EOF, "(?i)there are stopped jobs"])
        if index==1:
            self.sendline("exit")
            self.expect(EOF)
        self.close()

    def prompt(self, timeout=-1):
        '''Match the next shell prompt.

        This is little more than a short-cut to the :meth:`~pexpect.spawn.expect`
        method. Note that if you called :meth:`login` with
        ``auto_prompt_reset=False``, then before calling :meth:`prompt` you must
        set the :attr:`PROMPT` attribute to a regex that it will use for
        matching the prompt.

        Calling :meth:`prompt` will erase the contents of the :attr:`before`
        attribute even if no prompt is ever matched. If timeout is not given or
        it is set to -1 then self.timeout is used.

        :return: True if the shell prompt was matched, False if the timeout was
                 reached.
        '''

        if timeout == -1:
            timeout = self.timeout
        i = self.expect([self.PROMPT, TIMEOUT], timeout=timeout)
        if i==1:
            return False
        return True

    def set_unique_prompt(self):
        '''This sets the remote prompt to something more unique than ``#`` or ``$``.
        This makes it easier for the :meth:`prompt` method to match the shell prompt
        unambiguously. This method is called automatically by the :meth:`login`
        method, but you may want to call it manually if you somehow reset the
        shell prompt. For example, if you 'su' to a different user then you
        will need to manually reset the prompt. This sends shell commands to
        the remote host to set the prompt, so this assumes the remote host is
        ready to receive commands.

        Alternatively, you may use your own prompt pattern. In this case you
        should call :meth:`login` with ``auto_prompt_reset=False``; then set the
        :attr:`PROMPT` attribute to a regular expression. After that, the
        :meth:`prompt` method will try to match your prompt pattern.
        '''

        self.sendline("unset PROMPT_COMMAND")
        self.sendline(self.PROMPT_SET_SH) # sh-style
        i = self.expect ([TIMEOUT, self.PROMPT], timeout=10)
        if i == 0: # csh-style
            self.sendline(self.PROMPT_SET_CSH)
            i = self.expect([TIMEOUT, self.PROMPT], timeout=10)
            if i == 0: # zsh-style
                self.sendline(self.PROMPT_SET_ZSH)
                i = self.expect([TIMEOUT, self.PROMPT], timeout=10)
                if i == 0:
                    return False
        return True

# vi:ts=4:sw=4:expandtab:ft=python:
