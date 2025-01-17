import sys
import types

from .exceptions import EOF, TIMEOUT
from .pty_spawn import spawn

def run(command, timeout=30, withexitstatus=False, events=None,
        extra_args=None, logfile=None, cwd=None, env=None, **kwargs):

    '''
    This function runs the given command; waits for it to finish; then
    returns all output as a string. STDERR is included in output. If the full
    path to the command is not given then the path is searched.

    Note that lines are terminated by CR/LF (\\r\\n) combination even on
    UNIX-like systems because this is the standard for pseudottys. If you set
    'withexitstatus' to true, then run will return a tuple of (command_output,
    exitstatus). If 'withexitstatus' is false then this returns just
    command_output.

    The run() function can often be used instead of creating a spawn instance.
    For example, the following code uses spawn::

        from pexpect import *
        child = spawn('scp foo user@example.com:.')
        child.expect('(?i)password')
        child.sendline(mypassword)

    The previous code can be replace with the following::

        from pexpect import *
        run('scp foo user@example.com:.', events={'(?i)password': mypassword})

    **Examples**

    Start the apache daemon on the local machine::

        from pexpect import *
        run("/usr/local/apache/bin/apachectl start")

    Check in a file using SVN::

        from pexpect import *
        run("svn ci -m 'automatic commit' my_file.py")

    Run a command and capture exit status::

        from pexpect import *
        (command_output, exitstatus) = run('ls -l /bin', withexitstatus=1)

    The following will run SSH and execute 'ls -l' on the remote machine. The
    password 'secret' will be sent if the '(?i)password' pattern is ever seen::

        run("ssh username@machine.example.com 'ls -l'",
            events={'(?i)password':'secret\\n'})

    This will start mencoder to rip a video from DVD. This will also display
    progress ticks every 5 seconds as it runs. For example::

        from pexpect import *
        def print_ticks(d):
            print d['event_count'],
        run("mencoder dvd://1 -o video.avi -oac copy -ovc copy",
            events={TIMEOUT:print_ticks}, timeout=5)

    The 'events' argument should be either a dictionary or a tuple list that
    contains patterns and responses. Whenever one of the patterns is seen
    in the command output, run() will send the associated response string.
    So, run() in the above example can be also written as::

        run("mencoder dvd://1 -o video.avi -oac copy -ovc copy",
            events=[(TIMEOUT,print_ticks)], timeout=5)

    Use a tuple list for events if the command output requires a delicate
    control over what pattern should be matched, since the tuple list is passed
    to pexpect() as its pattern list, with the order of patterns preserved.

    Note that you should put newlines in your string if Enter is necessary.

    Like the example above, the responses may also contain a callback, either
    a function or method.  It should accept a dictionary value as an argument.
    The dictionary contains all the locals from the run() function, so you can
    access the child spawn object or any other variable defined in run()
    (event_count, child, and extra_args are the most useful). A callback may
    return True to stop the current run process.  Otherwise run() continues
    until the next event. A callback may also return a string which will be
    sent to the child. 'extra_args' is not used by directly run(). It provides
    a way to pass data to a callback function through run() through the locals
    dictionary passed to a callback.

    Like :class:`spawn`, passing *encoding* will make it work with unicode
    instead of bytes. You can pass *codec_errors* to control how errors in
    encoding and decoding are handled.
    '''
    if timeout == -1:
        child = spawn(command, maxread=2000, logfile=logfile, cwd=cwd, env=env,
                        **kwargs)
    else:
        child = spawn(command, timeout=timeout, maxread=2000, logfile=logfile,
                cwd=cwd, env=env, **kwargs)
    if isinstance(events, list):
        patterns= [x for x,y in events]
        responses = [y for x,y in events]
    elif isinstance(events, dict):
        patterns = list(events.keys())
        responses = list(events.values())
    else:
        # This assumes EOF or TIMEOUT will eventually cause run to terminate.
        patterns = None
        responses = None
    child_result_list = []
    event_count = 0
    while True:
        try:
            index = child.expect(patterns)
            if isinstance(child.after, child.allowed_string_types):
                child_result_list.append(child.before + child.after)
            else:
                # child.after may have been a TIMEOUT or EOF,
                # which we don't want appended to the list.
                child_result_list.append(child.before)
            if isinstance(responses[index], child.allowed_string_types):
                child.send(responses[index])
            elif (isinstance(responses[index], types.FunctionType) or
                  isinstance(responses[index], types.MethodType)):
                callback_result = responses[index](locals())
                sys.stdout.flush()
                if isinstance(callback_result, child.allowed_string_types):
                    child.send(callback_result)
                elif callback_result:
                    break
            else:
                raise TypeError("parameter `event' at index {index} must be "
                                "a string, method, or function: {value!r}"
                                .format(index=index, value=responses[index]))
            event_count = event_count + 1
        except TIMEOUT:
            child_result_list.append(child.before)
            break
        except EOF:
            child_result_list.append(child.before)
            break
    child_result = child.string_type().join(child_result_list)
    if withexitstatus:
        child.close()
        return (child_result, child.exitstatus)
    else:
        return child_result

def runu(command, timeout=30, withexitstatus=False, events=None,
        extra_args=None, logfile=None, cwd=None, env=None, **kwargs):
    """Deprecated: pass encoding to run() instead.
    """
    kwargs.setdefault('encoding', 'utf-8')
    return run(command, timeout=timeout, withexitstatus=withexitstatus,
                events=events, extra_args=extra_args, logfile=logfile, cwd=cwd,
                env=env, **kwargs)
