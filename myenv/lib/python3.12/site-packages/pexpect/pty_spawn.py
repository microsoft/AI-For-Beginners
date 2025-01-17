import os
import sys
import time
import pty
import tty
import errno
import signal
from contextlib import contextmanager

import ptyprocess
from ptyprocess.ptyprocess import use_native_pty_fork

from .exceptions import ExceptionPexpect, EOF, TIMEOUT
from .spawnbase import SpawnBase
from .utils import (
    which, split_command_line, select_ignore_interrupts, poll_ignore_interrupts
)

@contextmanager
def _wrap_ptyprocess_err():
    """Turn ptyprocess errors into our own ExceptionPexpect errors"""
    try:
        yield
    except ptyprocess.PtyProcessError as e:
        raise ExceptionPexpect(*e.args)

PY3 = (sys.version_info[0] >= 3)

class spawn(SpawnBase):
    '''This is the main class interface for Pexpect. Use this class to start
    and control child applications. '''

    # This is purely informational now - changing it has no effect
    use_native_pty_fork = use_native_pty_fork

    def __init__(self, command, args=[], timeout=30, maxread=2000,
                 searchwindowsize=None, logfile=None, cwd=None, env=None,
                 ignore_sighup=False, echo=True, preexec_fn=None,
                 encoding=None, codec_errors='strict', dimensions=None,
                 use_poll=False):
        '''This is the constructor. The command parameter may be a string that
        includes a command and any arguments to the command. For example::

            child = pexpect.spawn('/usr/bin/ftp')
            child = pexpect.spawn('/usr/bin/ssh user@example.com')
            child = pexpect.spawn('ls -latr /tmp')

        You may also construct it with a list of arguments like so::

            child = pexpect.spawn('/usr/bin/ftp', [])
            child = pexpect.spawn('/usr/bin/ssh', ['user@example.com'])
            child = pexpect.spawn('ls', ['-latr', '/tmp'])

        After this the child application will be created and will be ready to
        talk to. For normal use, see expect() and send() and sendline().

        Remember that Pexpect does NOT interpret shell meta characters such as
        redirect, pipe, or wild cards (``>``, ``|``, or ``*``). This is a
        common mistake.  If you want to run a command and pipe it through
        another command then you must also start a shell. For example::

            child = pexpect.spawn('/bin/bash -c "ls -l | grep LOG > logs.txt"')
            child.expect(pexpect.EOF)

        The second form of spawn (where you pass a list of arguments) is useful
        in situations where you wish to spawn a command and pass it its own
        argument list. This can make syntax more clear. For example, the
        following is equivalent to the previous example::

            shell_cmd = 'ls -l | grep LOG > logs.txt'
            child = pexpect.spawn('/bin/bash', ['-c', shell_cmd])
            child.expect(pexpect.EOF)

        The maxread attribute sets the read buffer size. This is maximum number
        of bytes that Pexpect will try to read from a TTY at one time. Setting
        the maxread size to 1 will turn off buffering. Setting the maxread
        value higher may help performance in cases where large amounts of
        output are read back from the child. This feature is useful in
        conjunction with searchwindowsize.

        When the keyword argument *searchwindowsize* is None (default), the
        full buffer is searched at each iteration of receiving incoming data.
        The default number of bytes scanned at each iteration is very large
        and may be reduced to collaterally reduce search cost.  After
        :meth:`~.expect` returns, the full buffer attribute remains up to
        size *maxread* irrespective of *searchwindowsize* value.

        When the keyword argument ``timeout`` is specified as a number,
        (default: *30*), then :class:`TIMEOUT` will be raised after the value
        specified has elapsed, in seconds, for any of the :meth:`~.expect`
        family of method calls.  When None, TIMEOUT will not be raised, and
        :meth:`~.expect` may block indefinitely until match.


        The logfile member turns on or off logging. All input and output will
        be copied to the given file object. Set logfile to None to stop
        logging. This is the default. Set logfile to sys.stdout to echo
        everything to standard output. The logfile is flushed after each write.

        Example log input and output to a file::

            child = pexpect.spawn('some_command')
            fout = open('mylog.txt','wb')
            child.logfile = fout

        Example log to stdout::

            # In Python 2:
            child = pexpect.spawn('some_command')
            child.logfile = sys.stdout

            # In Python 3, we'll use the ``encoding`` argument to decode data
            # from the subprocess and handle it as unicode:
            child = pexpect.spawn('some_command', encoding='utf-8')
            child.logfile = sys.stdout

        The logfile_read and logfile_send members can be used to separately log
        the input from the child and output sent to the child. Sometimes you
        don't want to see everything you write to the child. You only want to
        log what the child sends back. For example::

            child = pexpect.spawn('some_command')
            child.logfile_read = sys.stdout

        You will need to pass an encoding to spawn in the above code if you are
        using Python 3.

        To separately log output sent to the child use logfile_send::

            child.logfile_send = fout

        If ``ignore_sighup`` is True, the child process will ignore SIGHUP
        signals. The default is False from Pexpect 4.0, meaning that SIGHUP
        will be handled normally by the child.

        The delaybeforesend helps overcome a weird behavior that many users
        were experiencing. The typical problem was that a user would expect() a
        "Password:" prompt and then immediately call sendline() to send the
        password. The user would then see that their password was echoed back
        to them. Passwords don't normally echo. The problem is caused by the
        fact that most applications print out the "Password" prompt and then
        turn off stdin echo, but if you send your password before the
        application turned off echo, then you get your password echoed.
        Normally this wouldn't be a problem when interacting with a human at a
        real keyboard. If you introduce a slight delay just before writing then
        this seems to clear up the problem. This was such a common problem for
        many users that I decided that the default pexpect behavior should be
        to sleep just before writing to the child application. 1/20th of a
        second (50 ms) seems to be enough to clear up the problem. You can set
        delaybeforesend to None to return to the old behavior.

        Note that spawn is clever about finding commands on your path.
        It uses the same logic that "which" uses to find executables.

        If you wish to get the exit status of the child you must call the
        close() method. The exit or signal status of the child will be stored
        in self.exitstatus or self.signalstatus. If the child exited normally
        then exitstatus will store the exit return code and signalstatus will
        be None. If the child was terminated abnormally with a signal then
        signalstatus will store the signal value and exitstatus will be None::

            child = pexpect.spawn('some_command')
            child.close()
            print(child.exitstatus, child.signalstatus)

        If you need more detail you can also read the self.status member which
        stores the status returned by os.waitpid. You can interpret this using
        os.WIFEXITED/os.WEXITSTATUS or os.WIFSIGNALED/os.TERMSIG.

        The echo attribute may be set to False to disable echoing of input.
        As a pseudo-terminal, all input echoed by the "keyboard" (send()
        or sendline()) will be repeated to output.  For many cases, it is
        not desirable to have echo enabled, and it may be later disabled
        using setecho(False) followed by waitnoecho().  However, for some
        platforms such as Solaris, this is not possible, and should be
        disabled immediately on spawn.

        If preexec_fn is given, it will be called in the child process before
        launching the given command. This is useful to e.g. reset inherited
        signal handlers.

        The dimensions attribute specifies the size of the pseudo-terminal as
        seen by the subprocess, and is specified as a two-entry tuple (rows,
        columns). If this is unspecified, the defaults in ptyprocess will apply.

        The use_poll attribute enables using select.poll() over select.select()
        for socket handling. This is handy if your system could have > 1024 fds
        '''
        super(spawn, self).__init__(timeout=timeout, maxread=maxread, searchwindowsize=searchwindowsize,
                                    logfile=logfile, encoding=encoding, codec_errors=codec_errors)
        self.STDIN_FILENO = pty.STDIN_FILENO
        self.STDOUT_FILENO = pty.STDOUT_FILENO
        self.STDERR_FILENO = pty.STDERR_FILENO
        self.str_last_chars = 100
        self.cwd = cwd
        self.env = env
        self.echo = echo
        self.ignore_sighup = ignore_sighup
        self.__irix_hack = sys.platform.lower().startswith('irix')
        if command is None:
            self.command = None
            self.args = None
            self.name = '<pexpect factory incomplete>'
        else:
            self._spawn(command, args, preexec_fn, dimensions)
        self.use_poll = use_poll

    def __str__(self):
        '''This returns a human-readable string that represents the state of
        the object. '''

        s = []
        s.append(repr(self))
        s.append('command: ' + str(self.command))
        s.append('args: %r' % (self.args,))
        s.append('buffer (last %s chars): %r' % (self.str_last_chars,self.buffer[-self.str_last_chars:]))
        s.append('before (last %s chars): %r' % (self.str_last_chars,self.before[-self.str_last_chars:] if self.before else ''))
        s.append('after: %r' % (self.after,))
        s.append('match: %r' % (self.match,))
        s.append('match_index: ' + str(self.match_index))
        s.append('exitstatus: ' + str(self.exitstatus))
        if hasattr(self, 'ptyproc'):
            s.append('flag_eof: ' + str(self.flag_eof))
        s.append('pid: ' + str(self.pid))
        s.append('child_fd: ' + str(self.child_fd))
        s.append('closed: ' + str(self.closed))
        s.append('timeout: ' + str(self.timeout))
        s.append('delimiter: ' + str(self.delimiter))
        s.append('logfile: ' + str(self.logfile))
        s.append('logfile_read: ' + str(self.logfile_read))
        s.append('logfile_send: ' + str(self.logfile_send))
        s.append('maxread: ' + str(self.maxread))
        s.append('ignorecase: ' + str(self.ignorecase))
        s.append('searchwindowsize: ' + str(self.searchwindowsize))
        s.append('delaybeforesend: ' + str(self.delaybeforesend))
        s.append('delayafterclose: ' + str(self.delayafterclose))
        s.append('delayafterterminate: ' + str(self.delayafterterminate))
        return '\n'.join(s)

    def _spawn(self, command, args=[], preexec_fn=None, dimensions=None):
        '''This starts the given command in a child process. This does all the
        fork/exec type of stuff for a pty. This is called by __init__. If args
        is empty then command will be parsed (split on spaces) and args will be
        set to parsed arguments. '''

        # The pid and child_fd of this object get set by this method.
        # Note that it is difficult for this method to fail.
        # You cannot detect if the child process cannot start.
        # So the only way you can tell if the child process started
        # or not is to try to read from the file descriptor. If you get
        # EOF immediately then it means that the child is already dead.
        # That may not necessarily be bad because you may have spawned a child
        # that performs some task; creates no stdout output; and then dies.

        # If command is an int type then it may represent a file descriptor.
        if isinstance(command, type(0)):
            raise ExceptionPexpect('Command is an int type. ' +
                    'If this is a file descriptor then maybe you want to ' +
                    'use fdpexpect.fdspawn which takes an existing ' +
                    'file descriptor instead of a command string.')

        if not isinstance(args, type([])):
            raise TypeError('The argument, args, must be a list.')

        if args == []:
            self.args = split_command_line(command)
            self.command = self.args[0]
        else:
            # Make a shallow copy of the args list.
            self.args = args[:]
            self.args.insert(0, command)
            self.command = command

        command_with_path = which(self.command, env=self.env)
        if command_with_path is None:
            raise ExceptionPexpect('The command was not found or was not ' +
                    'executable: %s.' % self.command)
        self.command = command_with_path
        self.args[0] = self.command

        self.name = '<' + ' '.join(self.args) + '>'

        assert self.pid is None, 'The pid member must be None.'
        assert self.command is not None, 'The command member must not be None.'

        kwargs = {'echo': self.echo, 'preexec_fn': preexec_fn}
        if self.ignore_sighup:
            def preexec_wrapper():
                "Set SIGHUP to be ignored, then call the real preexec_fn"
                signal.signal(signal.SIGHUP, signal.SIG_IGN)
                if preexec_fn is not None:
                    preexec_fn()
            kwargs['preexec_fn'] = preexec_wrapper

        if dimensions is not None:
            kwargs['dimensions'] = dimensions

        if self.encoding is not None:
            # Encode command line using the specified encoding
            self.args = [a if isinstance(a, bytes) else a.encode(self.encoding)
                         for a in self.args]

        self.ptyproc = self._spawnpty(self.args, env=self.env,
                                     cwd=self.cwd, **kwargs)

        self.pid = self.ptyproc.pid
        self.child_fd = self.ptyproc.fd


        self.terminated = False
        self.closed = False

    def _spawnpty(self, args, **kwargs):
        '''Spawn a pty and return an instance of PtyProcess.'''
        return ptyprocess.PtyProcess.spawn(args, **kwargs)

    def close(self, force=True):
        '''This closes the connection with the child application. Note that
        calling close() more than once is valid. This emulates standard Python
        behavior with files. Set force to True if you want to make sure that
        the child is terminated (SIGKILL is sent if the child ignores SIGHUP
        and SIGINT). '''

        self.flush()
        with _wrap_ptyprocess_err():
            # PtyProcessError may be raised if it is not possible to terminate
            # the child.
            self.ptyproc.close(force=force)
        self.isalive()  # Update exit status from ptyproc
        self.child_fd = -1
        self.closed = True

    def isatty(self):
        '''This returns True if the file descriptor is open and connected to a
        tty(-like) device, else False.

        On SVR4-style platforms implementing streams, such as SunOS and HP-UX,
        the child pty may not appear as a terminal device.  This means
        methods such as setecho(), setwinsize(), getwinsize() may raise an
        IOError. '''

        return os.isatty(self.child_fd)

    def waitnoecho(self, timeout=-1):
        '''This waits until the terminal ECHO flag is set False. This returns
        True if the echo mode is off. This returns False if the ECHO flag was
        not set False before the timeout. This can be used to detect when the
        child is waiting for a password. Usually a child application will turn
        off echo mode when it is waiting for the user to enter a password. For
        example, instead of expecting the "password:" prompt you can wait for
        the child to set ECHO off::

            p = pexpect.spawn('ssh user@example.com')
            p.waitnoecho()
            p.sendline(mypassword)

        If timeout==-1 then this method will use the value in self.timeout.
        If timeout==None then this method to block until ECHO flag is False.
        '''

        if timeout == -1:
            timeout = self.timeout
        if timeout is not None:
            end_time = time.time() + timeout
        while True:
            if not self.getecho():
                return True
            if timeout < 0 and timeout is not None:
                return False
            if timeout is not None:
                timeout = end_time - time.time()
            time.sleep(0.1)

    def getecho(self):
        '''This returns the terminal echo mode. This returns True if echo is
        on or False if echo is off. Child applications that are expecting you
        to enter a password often set ECHO False. See waitnoecho().

        Not supported on platforms where ``isatty()`` returns False.  '''
        return self.ptyproc.getecho()

    def setecho(self, state):
        '''This sets the terminal echo mode on or off. Note that anything the
        child sent before the echo will be lost, so you should be sure that
        your input buffer is empty before you call setecho(). For example, the
        following will work as expected::

            p = pexpect.spawn('cat') # Echo is on by default.
            p.sendline('1234') # We expect see this twice from the child...
            p.expect(['1234']) # ... once from the tty echo...
            p.expect(['1234']) # ... and again from cat itself.
            p.setecho(False) # Turn off tty echo
            p.sendline('abcd') # We will set this only once (echoed by cat).
            p.sendline('wxyz') # We will set this only once (echoed by cat)
            p.expect(['abcd'])
            p.expect(['wxyz'])

        The following WILL NOT WORK because the lines sent before the setecho
        will be lost::

            p = pexpect.spawn('cat')
            p.sendline('1234')
            p.setecho(False) # Turn off tty echo
            p.sendline('abcd') # We will set this only once (echoed by cat).
            p.sendline('wxyz') # We will set this only once (echoed by cat)
            p.expect(['1234'])
            p.expect(['1234'])
            p.expect(['abcd'])
            p.expect(['wxyz'])


        Not supported on platforms where ``isatty()`` returns False.
        '''
        return self.ptyproc.setecho(state)

    def read_nonblocking(self, size=1, timeout=-1):
        '''This reads at most size characters from the child application. It
        includes a timeout. If the read does not complete within the timeout
        period then a TIMEOUT exception is raised. If the end of file is read
        then an EOF exception will be raised.  If a logfile is specified, a
        copy is written to that log.

        If timeout is None then the read may block indefinitely.
        If timeout is -1 then the self.timeout value is used. If timeout is 0
        then the child is polled and if there is no data immediately ready
        then this will raise a TIMEOUT exception.

        The timeout refers only to the amount of time to read at least one
        character. This is not affected by the 'size' parameter, so if you call
        read_nonblocking(size=100, timeout=30) and only one character is
        available right away then one character will be returned immediately.
        It will not wait for 30 seconds for another 99 characters to come in.

        On the other hand, if there are bytes available to read immediately,
        all those bytes will be read (up to the buffer size). So, if the
        buffer size is 1 megabyte and there is 1 megabyte of data available
        to read, the buffer will be filled, regardless of timeout.

        This is a wrapper around os.read(). It uses select.select() or
        select.poll() to implement the timeout. '''

        if self.closed:
            raise ValueError('I/O operation on closed file.')

        if self.use_poll:
            def select(timeout):
                return poll_ignore_interrupts([self.child_fd], timeout)
        else:
            def select(timeout):
                return select_ignore_interrupts([self.child_fd], [], [], timeout)[0]

        # If there is data available to read right now, read as much as
        # we can. We do this to increase performance if there are a lot
        # of bytes to be read. This also avoids calling isalive() too
        # often. See also:
        # * https://github.com/pexpect/pexpect/pull/304
        # * http://trac.sagemath.org/ticket/10295
        if select(0):
            try:
                incoming = super(spawn, self).read_nonblocking(size)
            except EOF:
                # Maybe the child is dead: update some attributes in that case
                self.isalive()
                raise
            while len(incoming) < size and select(0):
                try:
                    incoming += super(spawn, self).read_nonblocking(size - len(incoming))
                except EOF:
                    # Maybe the child is dead: update some attributes in that case
                    self.isalive()
                    # Don't raise EOF, just return what we read so far.
                    return incoming
            return incoming

        if timeout == -1:
            timeout = self.timeout

        if not self.isalive():
            # The process is dead, but there may or may not be data
            # available to read. Note that some systems such as Solaris
            # do not give an EOF when the child dies. In fact, you can
            # still try to read from the child_fd -- it will block
            # forever or until TIMEOUT. For that reason, it's important
            # to do this check before calling select() with timeout.
            if select(0):
                return super(spawn, self).read_nonblocking(size)
            self.flag_eof = True
            raise EOF('End Of File (EOF). Braindead platform.')
        elif self.__irix_hack:
            # Irix takes a long time before it realizes a child was terminated.
            # Make sure that the timeout is at least 2 seconds.
            # FIXME So does this mean Irix systems are forced to always have
            # FIXME a 2 second delay when calling read_nonblocking? That sucks.
            if timeout is not None and timeout < 2:
                timeout = 2

        # Because of the select(0) check above, we know that no data
        # is available right now. But if a non-zero timeout is given
        # (possibly timeout=None), we call select() with a timeout.
        if (timeout != 0) and select(timeout):
            return super(spawn, self).read_nonblocking(size)

        if not self.isalive():
            # Some platforms, such as Irix, will claim that their
            # processes are alive; timeout on the select; and
            # then finally admit that they are not alive.
            self.flag_eof = True
            raise EOF('End of File (EOF). Very slow platform.')
        else:
            raise TIMEOUT('Timeout exceeded.')

    def write(self, s):
        '''This is similar to send() except that there is no return value.
        '''

        self.send(s)

    def writelines(self, sequence):
        '''This calls write() for each element in the sequence. The sequence
        can be any iterable object producing strings, typically a list of
        strings. This does not add line separators. There is no return value.
        '''

        for s in sequence:
            self.write(s)

    def send(self, s):
        '''Sends string ``s`` to the child process, returning the number of
        bytes written. If a logfile is specified, a copy is written to that
        log.

        The default terminal input mode is canonical processing unless set
        otherwise by the child process. This allows backspace and other line
        processing to be performed prior to transmitting to the receiving
        program. As this is buffered, there is a limited size of such buffer.

        On Linux systems, this is 4096 (defined by N_TTY_BUF_SIZE). All
        other systems honor the POSIX.1 definition PC_MAX_CANON -- 1024
        on OSX, 256 on OpenSolaris, and 1920 on FreeBSD.

        This value may be discovered using fpathconf(3)::

            >>> from os import fpathconf
            >>> print(fpathconf(0, 'PC_MAX_CANON'))
            256

        On such a system, only 256 bytes may be received per line. Any
        subsequent bytes received will be discarded. BEL (``'\a'``) is then
        sent to output if IMAXBEL (termios.h) is set by the tty driver.
        This is usually enabled by default.  Linux does not honor this as
        an option -- it behaves as though it is always set on.

        Canonical input processing may be disabled altogether by executing
        a shell, then stty(1), before executing the final program::

            >>> bash = pexpect.spawn('/bin/bash', echo=False)
            >>> bash.sendline('stty -icanon')
            >>> bash.sendline('base64')
            >>> bash.sendline('x' * 5000)
        '''

        if self.delaybeforesend is not None:
            time.sleep(self.delaybeforesend)

        s = self._coerce_send_string(s)
        self._log(s, 'send')

        b = self._encoder.encode(s, final=False)
        return os.write(self.child_fd, b)

    def sendline(self, s=''):
        '''Wraps send(), sending string ``s`` to child process, with
        ``os.linesep`` automatically appended. Returns number of bytes
        written.  Only a limited number of bytes may be sent for each
        line in the default terminal mode, see docstring of :meth:`send`.
        '''
        s = self._coerce_send_string(s)
        return self.send(s + self.linesep)

    def _log_control(self, s):
        """Write control characters to the appropriate log files"""
        if self.encoding is not None:
            s = s.decode(self.encoding, 'replace')
        self._log(s, 'send')

    def sendcontrol(self, char):
        '''Helper method that wraps send() with mnemonic access for sending control
        character to the child (such as Ctrl-C or Ctrl-D).  For example, to send
        Ctrl-G (ASCII 7, bell, '\a')::

            child.sendcontrol('g')

        See also, sendintr() and sendeof().
        '''
        n, byte = self.ptyproc.sendcontrol(char)
        self._log_control(byte)
        return n

    def sendeof(self):
        '''This sends an EOF to the child. This sends a character which causes
        the pending parent output buffer to be sent to the waiting child
        program without waiting for end-of-line. If it is the first character
        of the line, the read() in the user program returns 0, which signifies
        end-of-file. This means to work as expected a sendeof() has to be
        called at the beginning of a line. This method does not send a newline.
        It is the responsibility of the caller to ensure the eof is sent at the
        beginning of a line. '''

        n, byte = self.ptyproc.sendeof()
        self._log_control(byte)

    def sendintr(self):
        '''This sends a SIGINT to the child. It does not require
        the SIGINT to be the first character on a line. '''

        n, byte = self.ptyproc.sendintr()
        self._log_control(byte)

    @property
    def flag_eof(self):
        return self.ptyproc.flag_eof

    @flag_eof.setter
    def flag_eof(self, value):
        self.ptyproc.flag_eof = value

    def eof(self):
        '''This returns True if the EOF exception was ever raised.
        '''
        return self.flag_eof

    def terminate(self, force=False):
        '''This forces a child process to terminate. It starts nicely with
        SIGHUP and SIGINT. If "force" is True then moves onto SIGKILL. This
        returns True if the child was terminated. This returns False if the
        child could not be terminated. '''

        if not self.isalive():
            return True
        try:
            self.kill(signal.SIGHUP)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            self.kill(signal.SIGCONT)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            self.kill(signal.SIGINT)
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            if force:
                self.kill(signal.SIGKILL)
                time.sleep(self.delayafterterminate)
                if not self.isalive():
                    return True
                else:
                    return False
            return False
        except OSError:
            # I think there are kernel timing issues that sometimes cause
            # this to happen. I think isalive() reports True, but the
            # process is dead to the kernel.
            # Make one last attempt to see if the kernel is up to date.
            time.sleep(self.delayafterterminate)
            if not self.isalive():
                return True
            else:
                return False

    def wait(self):
        '''This waits until the child exits. This is a blocking call. This will
        not read any data from the child, so this will block forever if the
        child has unread output and has terminated. In other words, the child
        may have printed output then called exit(), but, the child is
        technically still alive until its output is read by the parent.

        This method is non-blocking if :meth:`wait` has already been called
        previously or :meth:`isalive` method returns False.  It simply returns
        the previously determined exit status.
        '''

        ptyproc = self.ptyproc
        with _wrap_ptyprocess_err():
            # exception may occur if "Is some other process attempting
            # "job control with our child pid?"
            exitstatus = ptyproc.wait()
        self.status = ptyproc.status
        self.exitstatus = ptyproc.exitstatus
        self.signalstatus = ptyproc.signalstatus
        self.terminated = True

        return exitstatus

    def isalive(self):
        '''This tests if the child process is running or not. This is
        non-blocking. If the child was terminated then this will read the
        exitstatus or signalstatus of the child. This returns True if the child
        process appears to be running or False if not. It can take literally
        SECONDS for Solaris to return the right status. '''

        ptyproc = self.ptyproc
        with _wrap_ptyprocess_err():
            alive = ptyproc.isalive()

        if not alive:
            self.status = ptyproc.status
            self.exitstatus = ptyproc.exitstatus
            self.signalstatus = ptyproc.signalstatus
            self.terminated = True

        return alive

    def kill(self, sig):

        '''This sends the given signal to the child application. In keeping
        with UNIX tradition it has a misleading name. It does not necessarily
        kill the child unless you send the right signal. '''

        # Same as os.kill, but the pid is given for you.
        if self.isalive():
            os.kill(self.pid, sig)

    def getwinsize(self):
        '''This returns the terminal window size of the child tty. The return
        value is a tuple of (rows, cols). '''
        return self.ptyproc.getwinsize()

    def setwinsize(self, rows, cols):
        '''This sets the terminal window size of the child tty. This will cause
        a SIGWINCH signal to be sent to the child. This does not change the
        physical window size. It changes the size reported to TTY-aware
        applications like vi or curses -- applications that respond to the
        SIGWINCH signal. '''
        return self.ptyproc.setwinsize(rows, cols)


    def interact(self, escape_character=chr(29),
            input_filter=None, output_filter=None):

        '''This gives control of the child process to the interactive user (the
        human at the keyboard). Keystrokes are sent to the child process, and
        the stdout and stderr output of the child process is printed. This
        simply echos the child stdout and child stderr to the real stdout and
        it echos the real stdin to the child stdin. When the user types the
        escape_character this method will return None. The escape_character
        will not be transmitted.  The default for escape_character is
        entered as ``Ctrl - ]``, the very same as BSD telnet. To prevent
        escaping, escape_character may be set to None.

        If a logfile is specified, then the data sent and received from the
        child process in interact mode is duplicated to the given log.

        You may pass in optional input and output filter functions. These
        functions should take bytes array and return bytes array too. Even
        with ``encoding='utf-8'`` support, meth:`interact` will always pass
        input_filter and output_filter bytes. You may need to wrap your
        function to decode and encode back to UTF-8.

        The output_filter will be passed all the output from the child process.
        The input_filter will be passed all the keyboard input from the user.
        The input_filter is run BEFORE the check for the escape_character.

        Note that if you change the window size of the parent the SIGWINCH
        signal will not be passed through to the child. If you want the child
        window size to change when the parent's window size changes then do
        something like the following example::

            import pexpect, struct, fcntl, termios, signal, sys
            def sigwinch_passthrough (sig, data):
                s = struct.pack("HHHH", 0, 0, 0, 0)
                a = struct.unpack('hhhh', fcntl.ioctl(sys.stdout.fileno(),
                    termios.TIOCGWINSZ , s))
                if not p.closed:
                    p.setwinsize(a[0],a[1])

            # Note this 'p' is global and used in sigwinch_passthrough.
            p = pexpect.spawn('/bin/bash')
            signal.signal(signal.SIGWINCH, sigwinch_passthrough)
            p.interact()
        '''

        # Flush the buffer.
        self.write_to_stdout(self.buffer)
        self.stdout.flush()
        self._buffer = self.buffer_type()
        mode = tty.tcgetattr(self.STDIN_FILENO)
        tty.setraw(self.STDIN_FILENO)
        if escape_character is not None and PY3:
            escape_character = escape_character.encode('latin-1')
        try:
            self.__interact_copy(escape_character, input_filter, output_filter)
        finally:
            tty.tcsetattr(self.STDIN_FILENO, tty.TCSAFLUSH, mode)

    def __interact_writen(self, fd, data):
        '''This is used by the interact() method.
        '''

        while data != b'' and self.isalive():
            n = os.write(fd, data)
            data = data[n:]

    def __interact_read(self, fd):
        '''This is used by the interact() method.
        '''

        return os.read(fd, 1000)

    def __interact_copy(
        self, escape_character=None, input_filter=None, output_filter=None
    ):

        '''This is used by the interact() method.
        '''

        while self.isalive():
            if self.use_poll:
                r = poll_ignore_interrupts([self.child_fd, self.STDIN_FILENO])
            else:
                r, w, e = select_ignore_interrupts(
                    [self.child_fd, self.STDIN_FILENO], [], []
                )
            if self.child_fd in r:
                try:
                    data = self.__interact_read(self.child_fd)
                except OSError as err:
                    if err.args[0] == errno.EIO:
                        # Linux-style EOF
                        break
                    raise
                if data == b'':
                    # BSD-style EOF
                    break
                if output_filter:
                    data = output_filter(data)
                self._log(data, 'read')
                os.write(self.STDOUT_FILENO, data)
            if self.STDIN_FILENO in r:
                data = self.__interact_read(self.STDIN_FILENO)
                if input_filter:
                    data = input_filter(data)
                i = -1
                if escape_character is not None:
                    i = data.rfind(escape_character)
                if i != -1:
                    data = data[:i]
                    if data:
                        self._log(data, 'send')
                    self.__interact_writen(self.child_fd, data)
                    break
                self._log(data, 'send')
                self.__interact_writen(self.child_fd, data)


def spawnu(*args, **kwargs):
    """Deprecated: pass encoding to spawn() instead."""
    kwargs.setdefault('encoding', 'utf-8')
    return spawn(*args, **kwargs)
