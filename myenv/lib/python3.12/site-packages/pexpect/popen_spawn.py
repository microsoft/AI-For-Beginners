"""Provides an interface like pexpect.spawn interface using subprocess.Popen
"""
import os
import threading
import subprocess
import sys
import time
import signal
import shlex

try:
    from queue import Queue, Empty  # Python 3
except ImportError:
    from Queue import Queue, Empty  # Python 2

from .spawnbase import SpawnBase, PY3
from .exceptions import EOF
from .utils import string_types

class PopenSpawn(SpawnBase):
    def __init__(self, cmd, timeout=30, maxread=2000, searchwindowsize=None,
                 logfile=None, cwd=None, env=None, encoding=None,
                 codec_errors='strict', preexec_fn=None):
        super(PopenSpawn, self).__init__(timeout=timeout, maxread=maxread,
                searchwindowsize=searchwindowsize, logfile=logfile,
                encoding=encoding, codec_errors=codec_errors)

        # Note that `SpawnBase` initializes `self.crlf` to `\r\n`
        # because the default behaviour for a PTY is to convert
        # incoming LF to `\r\n` (see the `onlcr` flag and
        # https://stackoverflow.com/a/35887657/5397009). Here we set
        # it to `os.linesep` because that is what the spawned
        # application outputs by default and `popen` doesn't translate
        # anything.
        if encoding is None:
            self.crlf = os.linesep.encode ("ascii")
        else:
            self.crlf = self.string_type (os.linesep)

        kwargs = dict(bufsize=0, stdin=subprocess.PIPE,
                      stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
                      cwd=cwd, preexec_fn=preexec_fn, env=env)

        if sys.platform == 'win32':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            kwargs['startupinfo'] = startupinfo
            kwargs['creationflags'] = subprocess.CREATE_NEW_PROCESS_GROUP

        if isinstance(cmd, string_types) and sys.platform != 'win32':
            cmd = shlex.split(cmd, posix=os.name == 'posix')

        self.proc = subprocess.Popen(cmd, **kwargs)
        self.pid = self.proc.pid
        self.closed = False
        self._buf = self.string_type()

        self._read_queue = Queue()
        self._read_thread = threading.Thread(target=self._read_incoming)
        self._read_thread.daemon = True
        self._read_thread.start()

    _read_reached_eof = False

    def read_nonblocking(self, size, timeout):
        buf = self._buf
        if self._read_reached_eof:
            # We have already finished reading. Use up any buffered data,
            # then raise EOF
            if buf:
                self._buf = buf[size:]
                return buf[:size]
            else:
                self.flag_eof = True
                raise EOF('End Of File (EOF).')

        if timeout == -1:
            timeout = self.timeout
        elif timeout is None:
            timeout = 1e6

        t0 = time.time()
        while (time.time() - t0) < timeout and size and len(buf) < size:
            try:
                incoming = self._read_queue.get_nowait()
            except Empty:
                break
            else:
                if incoming is None:
                    self._read_reached_eof = True
                    break

                buf += self._decoder.decode(incoming, final=False)

        r, self._buf = buf[:size], buf[size:]

        self._log(r, 'read')
        return r

    def _read_incoming(self):
        """Run in a thread to move output from a pipe to a queue."""
        fileno = self.proc.stdout.fileno()
        while 1:
            buf = b''
            try:
                buf = os.read(fileno, 1024)
            except OSError as e:
                self._log(e, 'read')

            if not buf:
                # This indicates we have reached EOF
                self._read_queue.put(None)
                return

            self._read_queue.put(buf)

    def write(self, s):
        '''This is similar to send() except that there is no return value.
        '''
        self.send(s)

    def writelines(self, sequence):
        '''This calls write() for each element in the sequence.

        The sequence can be any iterable object producing strings, typically a
        list of strings. This does not add line separators. There is no return
        value.
        '''
        for s in sequence:
            self.send(s)

    def send(self, s):
        '''Send data to the subprocess' stdin.

        Returns the number of bytes written.
        '''
        s = self._coerce_send_string(s)
        self._log(s, 'send')

        b = self._encoder.encode(s, final=False)
        if PY3:
            return self.proc.stdin.write(b)
        else:
            # On Python 2, .write() returns None, so we return the length of
            # bytes written ourselves. This assumes they all got written.
            self.proc.stdin.write(b)
            return len(b)

    def sendline(self, s=''):
        '''Wraps send(), sending string ``s`` to child process, with os.linesep
        automatically appended. Returns number of bytes written. '''

        n = self.send(s)
        return n + self.send(self.linesep)

    def wait(self):
        '''Wait for the subprocess to finish.

        Returns the exit code.
        '''
        status = self.proc.wait()
        if status >= 0:
            self.exitstatus = status
            self.signalstatus = None
        else:
            self.exitstatus = None
            self.signalstatus = -status
        self.terminated = True
        return status

    def kill(self, sig):
        '''Sends a Unix signal to the subprocess.

        Use constants from the :mod:`signal` module to specify which signal.
        '''
        if sys.platform == 'win32':
            if sig in [signal.SIGINT, signal.CTRL_C_EVENT]:
                sig = signal.CTRL_C_EVENT
            elif sig in [signal.SIGBREAK, signal.CTRL_BREAK_EVENT]:
                sig = signal.CTRL_BREAK_EVENT
            else:
                sig = signal.SIGTERM

        os.kill(self.proc.pid, sig)

    def sendeof(self):
        '''Closes the stdin pipe from the writing end.'''
        self.proc.stdin.close()
