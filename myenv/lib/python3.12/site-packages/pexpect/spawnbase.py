from io import StringIO, BytesIO
import codecs
import os
import sys
import re
import errno
from .exceptions import ExceptionPexpect, EOF, TIMEOUT
from .expect import Expecter, searcher_string, searcher_re

PY3 = (sys.version_info[0] >= 3)
text_type = str if PY3 else unicode

class _NullCoder(object):
    """Pass bytes through unchanged."""
    @staticmethod
    def encode(b, final=False):
        return b

    @staticmethod
    def decode(b, final=False):
        return b

class SpawnBase(object):
    """A base class providing the backwards-compatible spawn API for Pexpect.

    This should not be instantiated directly: use :class:`pexpect.spawn` or
    :class:`pexpect.fdpexpect.fdspawn`.
    """
    encoding = None
    pid = None
    flag_eof = False

    def __init__(self, timeout=30, maxread=2000, searchwindowsize=None,
                 logfile=None, encoding=None, codec_errors='strict'):
        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.stderr = sys.stderr

        self.searcher = None
        self.ignorecase = False
        self.before = None
        self.after = None
        self.match = None
        self.match_index = None
        self.terminated = True
        self.exitstatus = None
        self.signalstatus = None
        # status returned by os.waitpid
        self.status = None
        # the child file descriptor is initially closed
        self.child_fd = -1
        self.timeout = timeout
        self.delimiter = EOF
        self.logfile = logfile
        # input from child (read_nonblocking)
        self.logfile_read = None
        # output to send (send, sendline)
        self.logfile_send = None
        # max bytes to read at one time into buffer
        self.maxread = maxread
        # Data before searchwindowsize point is preserved, but not searched.
        self.searchwindowsize = searchwindowsize
        # Delay used before sending data to child. Time in seconds.
        # Set this to None to skip the time.sleep() call completely.
        self.delaybeforesend = 0.05
        # Used by close() to give kernel time to update process status.
        # Time in seconds.
        self.delayafterclose = 0.1
        # Used by terminate() to give kernel time to update process status.
        # Time in seconds.
        self.delayafterterminate = 0.1
        # Delay in seconds to sleep after each call to read_nonblocking().
        # Set this to None to skip the time.sleep() call completely: that
        # would restore the behavior from pexpect-2.0 (for performance
        # reasons or because you don't want to release Python's global
        # interpreter lock).
        self.delayafterread = 0.0001
        self.softspace = False
        self.name = '<' + repr(self) + '>'
        self.closed = True

        # Unicode interface
        self.encoding = encoding
        self.codec_errors = codec_errors
        if encoding is None:
            # bytes mode (accepts some unicode for backwards compatibility)
            self._encoder = self._decoder = _NullCoder()
            self.string_type = bytes
            self.buffer_type = BytesIO
            self.crlf = b'\r\n'
            if PY3:
                self.allowed_string_types = (bytes, str)
                self.linesep = os.linesep.encode('ascii')
                def write_to_stdout(b):
                    try:
                        return sys.stdout.buffer.write(b)
                    except AttributeError:
                        # If stdout has been replaced, it may not have .buffer
                        return sys.stdout.write(b.decode('ascii', 'replace'))
                self.write_to_stdout = write_to_stdout
            else:
                self.allowed_string_types = (basestring,)  # analysis:ignore
                self.linesep = os.linesep
                self.write_to_stdout = sys.stdout.write
        else:
            # unicode mode
            self._encoder = codecs.getincrementalencoder(encoding)(codec_errors)
            self._decoder = codecs.getincrementaldecoder(encoding)(codec_errors)
            self.string_type = text_type
            self.buffer_type = StringIO
            self.crlf = u'\r\n'
            self.allowed_string_types = (text_type, )
            if PY3:
                self.linesep = os.linesep
            else:
                self.linesep = os.linesep.decode('ascii')
            # This can handle unicode in both Python 2 and 3
            self.write_to_stdout = sys.stdout.write
        # storage for async transport
        self.async_pw_transport = None
        # This is the read buffer. See maxread.
        self._buffer = self.buffer_type()
        # The buffer may be trimmed for efficiency reasons.  This is the
        # untrimmed buffer, used to create the before attribute.
        self._before = self.buffer_type()

    def _log(self, s, direction):
        if self.logfile is not None:
            self.logfile.write(s)
            self.logfile.flush()
        second_log = self.logfile_send if (direction=='send') else self.logfile_read
        if second_log is not None:
            second_log.write(s)
            second_log.flush()

    # For backwards compatibility, in bytes mode (when encoding is None)
    # unicode is accepted for send and expect. Unicode mode is strictly unicode
    # only.
    def _coerce_expect_string(self, s):
        if self.encoding is None and not isinstance(s, bytes):
            return s.encode('ascii')
        return s

    # In bytes mode, regex patterns should also be of bytes type
    def _coerce_expect_re(self, r):
        p = r.pattern
        if self.encoding is None and not isinstance(p, bytes):
            return re.compile(p.encode('utf-8'))
        # And vice-versa
        elif self.encoding is not None and isinstance(p, bytes):
            return re.compile(p.decode('utf-8'))
        return r

    def _coerce_send_string(self, s):
        if self.encoding is None and not isinstance(s, bytes):
            return s.encode('utf-8')
        return s

    def _get_buffer(self):
        return self._buffer.getvalue()

    def _set_buffer(self, value):
        self._buffer = self.buffer_type()
        self._buffer.write(value)

    # This property is provided for backwards compatibility (self.buffer used
    # to be a string/bytes object)
    buffer = property(_get_buffer, _set_buffer)

    def read_nonblocking(self, size=1, timeout=None):
        """This reads data from the file descriptor.

        This is a simple implementation suitable for a regular file. Subclasses using ptys or pipes should override it.

        The timeout parameter is ignored.
        """

        try:
            s = os.read(self.child_fd, size)
        except OSError as err:
            if err.args[0] == errno.EIO:
                # Linux-style EOF
                self.flag_eof = True
                raise EOF('End Of File (EOF). Exception style platform.')
            raise
        if s == b'':
            # BSD-style EOF
            self.flag_eof = True
            raise EOF('End Of File (EOF). Empty string style platform.')

        s = self._decoder.decode(s, final=False)
        self._log(s, 'read')
        return s

    def _pattern_type_err(self, pattern):
        raise TypeError('got {badtype} ({badobj!r}) as pattern, must be one'
                        ' of: {goodtypes}, pexpect.EOF, pexpect.TIMEOUT'\
                        .format(badtype=type(pattern),
                                badobj=pattern,
                                goodtypes=', '.join([str(ast)\
                                    for ast in self.allowed_string_types])
                                )
                        )

    def compile_pattern_list(self, patterns):
        '''This compiles a pattern-string or a list of pattern-strings.
        Patterns must be a StringType, EOF, TIMEOUT, SRE_Pattern, or a list of
        those. Patterns may also be None which results in an empty list (you
        might do this if waiting for an EOF or TIMEOUT condition without
        expecting any pattern).

        This is used by expect() when calling expect_list(). Thus expect() is
        nothing more than::

             cpl = self.compile_pattern_list(pl)
             return self.expect_list(cpl, timeout)

        If you are using expect() within a loop it may be more
        efficient to compile the patterns first and then call expect_list().
        This avoid calls in a loop to compile_pattern_list()::

             cpl = self.compile_pattern_list(my_pattern)
             while some_condition:
                ...
                i = self.expect_list(cpl, timeout)
                ...
        '''

        if patterns is None:
            return []
        if not isinstance(patterns, list):
            patterns = [patterns]

        # Allow dot to match \n
        compile_flags = re.DOTALL
        if self.ignorecase:
            compile_flags = compile_flags | re.IGNORECASE
        compiled_pattern_list = []
        for idx, p in enumerate(patterns):
            if isinstance(p, self.allowed_string_types):
                p = self._coerce_expect_string(p)
                compiled_pattern_list.append(re.compile(p, compile_flags))
            elif p is EOF:
                compiled_pattern_list.append(EOF)
            elif p is TIMEOUT:
                compiled_pattern_list.append(TIMEOUT)
            elif isinstance(p, type(re.compile(''))):
                p = self._coerce_expect_re(p)
                compiled_pattern_list.append(p)
            else:
                self._pattern_type_err(p)
        return compiled_pattern_list

    def expect(self, pattern, timeout=-1, searchwindowsize=-1, async_=False, **kw):
        '''This seeks through the stream until a pattern is matched. The
        pattern is overloaded and may take several types. The pattern can be a
        StringType, EOF, a compiled re, or a list of any of those types.
        Strings will be compiled to re types. This returns the index into the
        pattern list. If the pattern was not a list this returns index 0 on a
        successful match. This may raise exceptions for EOF or TIMEOUT. To
        avoid the EOF or TIMEOUT exceptions add EOF or TIMEOUT to the pattern
        list. That will cause expect to match an EOF or TIMEOUT condition
        instead of raising an exception.

        If you pass a list of patterns and more than one matches, the first
        match in the stream is chosen. If more than one pattern matches at that
        point, the leftmost in the pattern list is chosen. For example::

            # the input is 'foobar'
            index = p.expect(['bar', 'foo', 'foobar'])
            # returns 1('foo') even though 'foobar' is a "better" match

        Please note, however, that buffering can affect this behavior, since
        input arrives in unpredictable chunks. For example::

            # the input is 'foobar'
            index = p.expect(['foobar', 'foo'])
            # returns 0('foobar') if all input is available at once,
            # but returns 1('foo') if parts of the final 'bar' arrive late

        When a match is found for the given pattern, the class instance
        attribute *match* becomes an re.MatchObject result.  Should an EOF
        or TIMEOUT pattern match, then the match attribute will be an instance
        of that exception class.  The pairing before and after class
        instance attributes are views of the data preceding and following
        the matching pattern.  On general exception, class attribute
        *before* is all data received up to the exception, while *match* and
        *after* attributes are value None.

        When the keyword argument timeout is -1 (default), then TIMEOUT will
        raise after the default value specified by the class timeout
        attribute. When None, TIMEOUT will not be raised and may block
        indefinitely until match.

        When the keyword argument searchwindowsize is -1 (default), then the
        value specified by the class maxread attribute is used.

        A list entry may be EOF or TIMEOUT instead of a string. This will
        catch these exceptions and return the index of the list entry instead
        of raising the exception. The attribute 'after' will be set to the
        exception type. The attribute 'match' will be None. This allows you to
        write code like this::

                index = p.expect(['good', 'bad', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    do_something()
                elif index == 1:
                    do_something_else()
                elif index == 2:
                    do_some_other_thing()
                elif index == 3:
                    do_something_completely_different()

        instead of code like this::

                try:
                    index = p.expect(['good', 'bad'])
                    if index == 0:
                        do_something()
                    elif index == 1:
                        do_something_else()
                except EOF:
                    do_some_other_thing()
                except TIMEOUT:
                    do_something_completely_different()

        These two forms are equivalent. It all depends on what you want. You
        can also just expect the EOF if you are waiting for all output of a
        child to finish. For example::

                p = pexpect.spawn('/bin/ls')
                p.expect(pexpect.EOF)
                print p.before

        If you are trying to optimize for speed then see expect_list().

        On Python 3.4, or Python 3.3 with asyncio installed, passing
        ``async_=True``  will make this return an :mod:`asyncio` coroutine,
        which you can yield from to get the same result that this method would
        normally give directly. So, inside a coroutine, you can replace this code::

            index = p.expect(patterns)

        With this non-blocking form::

            index = yield from p.expect(patterns, async_=True)
        '''
        if 'async' in kw:
            async_ = kw.pop('async')
        if kw:
            raise TypeError("Unknown keyword arguments: {}".format(kw))

        compiled_pattern_list = self.compile_pattern_list(pattern)
        return self.expect_list(compiled_pattern_list,
                timeout, searchwindowsize, async_)

    def expect_list(self, pattern_list, timeout=-1, searchwindowsize=-1,
                    async_=False, **kw):
        '''This takes a list of compiled regular expressions and returns the
        index into the pattern_list that matched the child output. The list may
        also contain EOF or TIMEOUT(which are not compiled regular
        expressions). This method is similar to the expect() method except that
        expect_list() does not recompile the pattern list on every call. This
        may help if you are trying to optimize for speed, otherwise just use
        the expect() method.  This is called by expect().


        Like :meth:`expect`, passing ``async_=True`` will make this return an
        asyncio coroutine.
        '''
        if timeout == -1:
            timeout = self.timeout
        if 'async' in kw:
            async_ = kw.pop('async')
        if kw:
            raise TypeError("Unknown keyword arguments: {}".format(kw))

        exp = Expecter(self, searcher_re(pattern_list), searchwindowsize)
        if async_:
            from ._async import expect_async
            return expect_async(exp, timeout)
        else:
            return exp.expect_loop(timeout)

    def expect_exact(self, pattern_list, timeout=-1, searchwindowsize=-1,
                     async_=False, **kw):

        '''This is similar to expect(), but uses plain string matching instead
        of compiled regular expressions in 'pattern_list'. The 'pattern_list'
        may be a string; a list or other sequence of strings; or TIMEOUT and
        EOF.

        This call might be faster than expect() for two reasons: string
        searching is faster than RE matching and it is possible to limit the
        search to just the end of the input buffer.

        This method is also useful when you don't want to have to worry about
        escaping regular expression characters that you want to match.

        Like :meth:`expect`, passing ``async_=True`` will make this return an
        asyncio coroutine.
        '''
        if timeout == -1:
            timeout = self.timeout
        if 'async' in kw:
            async_ = kw.pop('async')
        if kw:
            raise TypeError("Unknown keyword arguments: {}".format(kw))

        if (isinstance(pattern_list, self.allowed_string_types) or
                pattern_list in (TIMEOUT, EOF)):
            pattern_list = [pattern_list]

        def prepare_pattern(pattern):
            if pattern in (TIMEOUT, EOF):
                return pattern
            if isinstance(pattern, self.allowed_string_types):
                return self._coerce_expect_string(pattern)
            self._pattern_type_err(pattern)

        try:
            pattern_list = iter(pattern_list)
        except TypeError:
            self._pattern_type_err(pattern_list)
        pattern_list = [prepare_pattern(p) for p in pattern_list]

        exp = Expecter(self, searcher_string(pattern_list), searchwindowsize)
        if async_:
            from ._async import expect_async
            return expect_async(exp, timeout)
        else:
            return exp.expect_loop(timeout)

    def expect_loop(self, searcher, timeout=-1, searchwindowsize=-1):
        '''This is the common loop used inside expect. The 'searcher' should be
        an instance of searcher_re or searcher_string, which describes how and
        what to search for in the input.

        See expect() for other arguments, return value and exceptions. '''

        exp = Expecter(self, searcher, searchwindowsize)
        return exp.expect_loop(timeout)

    def read(self, size=-1):
        '''This reads at most "size" bytes from the file (less if the read hits
        EOF before obtaining size bytes). If the size argument is negative or
        omitted, read all data until EOF is reached. The bytes are returned as
        a string object. An empty string is returned when EOF is encountered
        immediately. '''

        if size == 0:
            return self.string_type()
        if size < 0:
            # delimiter default is EOF
            self.expect(self.delimiter)
            return self.before

        # I could have done this more directly by not using expect(), but
        # I deliberately decided to couple read() to expect() so that
        # I would catch any bugs early and ensure consistent behavior.
        # It's a little less efficient, but there is less for me to
        # worry about if I have to later modify read() or expect().
        # Note, it's OK if size==-1 in the regex. That just means it
        # will never match anything in which case we stop only on EOF.
        cre = re.compile(self._coerce_expect_string('.{%d}' % size), re.DOTALL)
        # delimiter default is EOF
        index = self.expect([cre, self.delimiter])
        if index == 0:
            ### FIXME self.before should be ''. Should I assert this?
            return self.after
        return self.before

    def readline(self, size=-1):
        '''This reads and returns one entire line. The newline at the end of
        line is returned as part of the string, unless the file ends without a
        newline. An empty string is returned if EOF is encountered immediately.
        This looks for a newline as a CR/LF pair (\\r\\n) even on UNIX because
        this is what the pseudotty device returns. So contrary to what you may
        expect you will receive newlines as \\r\\n.

        If the size argument is 0 then an empty string is returned. In all
        other cases the size argument is ignored, which is not standard
        behavior for a file-like object. '''

        if size == 0:
            return self.string_type()
        # delimiter default is EOF
        index = self.expect([self.crlf, self.delimiter])
        if index == 0:
            return self.before + self.crlf
        else:
            return self.before

    def __iter__(self):
        '''This is to support iterators over a file-like object.
        '''
        return iter(self.readline, self.string_type())

    def readlines(self, sizehint=-1):
        '''This reads until EOF using readline() and returns a list containing
        the lines thus read. The optional 'sizehint' argument is ignored.
        Remember, because this reads until EOF that means the child
        process should have closed its stdout. If you run this method on
        a child that is still running with its stdout open then this
        method will block until it timesout.'''

        lines = []
        while True:
            line = self.readline()
            if not line:
                break
            lines.append(line)
        return lines

    def fileno(self):
        '''Expose file descriptor for a file-like interface
        '''
        return self.child_fd

    def flush(self):
        '''This does nothing. It is here to support the interface for a
        File-like object. '''
        pass

    def isatty(self):
        """Overridden in subclass using tty"""
        return False

    # For 'with spawn(...) as child:'
    def __enter__(self):
        return self

    def __exit__(self, etype, evalue, tb):
        # We rely on subclasses to implement close(). If they don't, it's not
        # clear what a context manager should do.
        self.close()
