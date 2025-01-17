# cython: freethreading_compatible = True
"""Cython backend for pyzmq"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

from __future__ import annotations

try:
    import cython

    if not cython.compiled:
        raise ImportError()
except ImportError:
    from pathlib import Path

    zmq_root = Path(__file__).parents[3]
    msg = f"""
    Attempting to import zmq Cython backend, which has not been compiled.

    This probably means you are importing zmq from its source tree.
    if this is what you want, make sure to do an in-place build first:

        pip install -e '{zmq_root}'

    If it is not, then '{zmq_root}' is probably on your sys.path,
    when it shouldn't be. Is that your current working directory?

    If neither of those is true and this file is actually installed,
    something seems to have gone wrong with the install!
    Please report at https://github.com/zeromq/pyzmq/issues
    """
    raise ImportError(msg)

import time
import warnings
from threading import Event
from weakref import ref

import cython as C
from cython import (
    NULL,
    Py_ssize_t,
    address,
    bint,
    cast,
    cclass,
    cfunc,
    char,
    declare,
    inline,
    nogil,
    p_char,
    p_void,
    pointer,
    size_t,
    sizeof,
)
from cython.cimports.cpython import (
    PyBytes_AsString,
    PyBytes_FromStringAndSize,
    PyBytes_Size,
    PyErr_CheckSignals,
)
from cython.cimports.libc.errno import EAGAIN, EINTR, ENAMETOOLONG, ENOENT, ENOTSOCK

# cimports require Cython 3
from cython.cimports.libc.stdint import uint32_t
from cython.cimports.libc.stdio import fprintf
from cython.cimports.libc.stdio import stderr as cstderr
from cython.cimports.libc.stdlib import free, malloc
from cython.cimports.libc.string import memcpy
from cython.cimports.zmq.backend.cython._externs import (
    get_ipc_path_max_len,
    getpid,
    mutex_allocate,
    mutex_lock,
    mutex_t,
    mutex_unlock,
)
from cython.cimports.zmq.backend.cython.libzmq import (
    ZMQ_ENOTSOCK,
    ZMQ_ETERM,
    ZMQ_EVENT_ALL,
    ZMQ_IDENTITY,
    ZMQ_IO_THREADS,
    ZMQ_LINGER,
    ZMQ_POLLIN,
    ZMQ_RCVMORE,
    ZMQ_ROUTER,
    ZMQ_SNDMORE,
    ZMQ_TYPE,
    ZMQ_VERSION_MAJOR,
    _zmq_version,
    fd_t,
    int64_t,
    zmq_bind,
    zmq_close,
    zmq_connect,
    zmq_ctx_destroy,
    zmq_ctx_get,
    zmq_ctx_new,
    zmq_ctx_set,
    zmq_curve_keypair,
    zmq_curve_public,
    zmq_device,
    zmq_disconnect,
    zmq_free_fn,
    zmq_getsockopt,
    zmq_has,
    zmq_init,
    zmq_join,
    zmq_leave,
    zmq_msg_close,
    zmq_msg_copy,
    zmq_msg_data,
    zmq_msg_get,
    zmq_msg_gets,
    zmq_msg_group,
    zmq_msg_init,
    zmq_msg_init_data,
    zmq_msg_init_size,
    zmq_msg_recv,
    zmq_msg_routing_id,
    zmq_msg_send,
    zmq_msg_set,
    zmq_msg_set_group,
    zmq_msg_set_routing_id,
    zmq_msg_size,
    zmq_msg_t,
    zmq_pollitem_t,
    zmq_proxy,
    zmq_proxy_steerable,
    zmq_setsockopt,
    zmq_socket,
    zmq_socket_monitor,
    zmq_strerror,
    zmq_unbind,
)
from cython.cimports.zmq.backend.cython.libzmq import zmq_errno as _zmq_errno
from cython.cimports.zmq.backend.cython.libzmq import zmq_poll as zmq_poll_c
from cython.cimports.zmq.utils.buffers import asbuffer_r

import zmq
from zmq.constants import SocketOption, _OptType
from zmq.error import InterruptedSystemCall, ZMQError, _check_version

IPC_PATH_MAX_LEN = get_ipc_path_max_len()


@cfunc
@inline
@C.exceptval(-1)
def _check_rc(rc: C.int, error_without_errno: bint = False) -> C.int:
    """internal utility for checking zmq return condition

    and raising the appropriate Exception class
    """
    errno: C.int = _zmq_errno()
    PyErr_CheckSignals()
    if errno == 0 and not error_without_errno:
        return 0
    if rc == -1:  # if rc < -1, it's a bug in libzmq. Should we warn?
        if errno == EINTR:
            from zmq.error import InterruptedSystemCall

            raise InterruptedSystemCall(errno)
        elif errno == EAGAIN:
            from zmq.error import Again

            raise Again(errno)
        elif errno == ZMQ_ETERM:
            from zmq.error import ContextTerminated

            raise ContextTerminated(errno)
        else:
            from zmq.error import ZMQError

            raise ZMQError(errno)
    return 0


# message Frame class

_zhint = C.struct(
    sock=p_void,
    mutex=pointer(mutex_t),
    id=size_t,
)


@cfunc
@nogil
def free_python_msg(data: p_void, vhint: p_void) -> C.int:
    """A pure-C function for DECREF'ing Python-owned message data.

    Sends a message on a PUSH socket

    The hint is a `zhint` struct with two values:

    sock (void *): pointer to the Garbage Collector's PUSH socket
    id (size_t): the id to be used to construct a zmq_msg_t that should be sent on a PUSH socket,
       signaling the Garbage Collector to remove its reference to the object.

    When the Garbage Collector's PULL socket receives the message,
    it deletes its reference to the object,
    allowing Python to free the memory.
    """
    msg = declare(zmq_msg_t)
    msg_ptr: pointer(zmq_msg_t) = address(msg)
    hint: pointer(_zhint) = cast(pointer(_zhint), vhint)
    rc: C.int

    if hint != NULL:
        zmq_msg_init_size(msg_ptr, sizeof(size_t))
        memcpy(zmq_msg_data(msg_ptr), address(hint.id), sizeof(size_t))
        rc = mutex_lock(hint.mutex)
        if rc != 0:
            fprintf(cstderr, "pyzmq-gc mutex lock failed rc=%d\n", rc)
        rc = zmq_msg_send(msg_ptr, hint.sock, 0)
        if rc < 0:
            # gc socket could have been closed, e.g. during process teardown.
            # If so, ignore the failure because there's nothing to do.
            if _zmq_errno() != ZMQ_ENOTSOCK:
                fprintf(
                    cstderr, "pyzmq-gc send failed: %s\n", zmq_strerror(_zmq_errno())
                )
        rc = mutex_unlock(hint.mutex)
        if rc != 0:
            fprintf(cstderr, "pyzmq-gc mutex unlock failed rc=%d\n", rc)

        zmq_msg_close(msg_ptr)
        free(hint)
        return 0


@cfunc
@inline
def _copy_zmq_msg_bytes(zmq_msg: pointer(zmq_msg_t)) -> bytes:
    """Copy the data from a zmq_msg_t"""
    data_c: p_char = NULL
    data_len_c: Py_ssize_t
    data_c = cast(p_char, zmq_msg_data(zmq_msg))
    data_len_c = zmq_msg_size(zmq_msg)
    return PyBytes_FromStringAndSize(data_c, data_len_c)


_gc = None


@cclass
class Frame:
    def __init__(
        self, data=None, track=False, copy=None, copy_threshold=None, **kwargs
    ):
        rc: C.int
        data_c: p_char = NULL
        data_len_c: Py_ssize_t = 0
        hint: pointer(_zhint)
        if copy_threshold is None:
            copy_threshold = zmq.COPY_THRESHOLD

        zmq_msg_ptr: pointer(zmq_msg_t) = address(self.zmq_msg)
        # init more as False
        self.more = False

        # Save the data object in case the user wants the the data as a str.
        self._data = data
        self._failed_init = True  # bool switch for dealloc
        self._buffer = None  # buffer view of data
        self._bytes = None  # bytes copy of data

        self.tracker_event = None
        self.tracker = None
        # self.tracker should start finished
        # except in the case where we are sharing memory with libzmq
        if track:
            self.tracker = zmq._FINISHED_TRACKER

        if isinstance(data, str):
            raise TypeError("Str objects not allowed. Only: bytes, buffer interfaces.")

        if data is None:
            rc = zmq_msg_init(zmq_msg_ptr)
            _check_rc(rc)
            self._failed_init = False
            return

        asbuffer_r(data, cast(pointer(p_void), address(data_c)), address(data_len_c))

        # copy unspecified, apply copy_threshold
        if copy is None:
            if copy_threshold and data_len_c < copy_threshold:
                copy = True
            else:
                copy = False

        if copy:
            # copy message data instead of sharing memory
            rc = zmq_msg_init_size(zmq_msg_ptr, data_len_c)
            _check_rc(rc)
            memcpy(zmq_msg_data(zmq_msg_ptr), data_c, data_len_c)
            self._failed_init = False
            return

        # Getting here means that we are doing a true zero-copy Frame,
        # where libzmq and Python are sharing memory.
        # Hook up garbage collection with MessageTracker and zmq_free_fn

        # Event and MessageTracker for monitoring when zmq is done with data:
        if track:
            evt = Event()
            self.tracker_event = evt
            self.tracker = zmq.MessageTracker(evt)
        # create the hint for zmq_free_fn
        # two pointers: the gc context and a message to be sent to the gc PULL socket
        # allows libzmq to signal to Python when it is done with Python-owned memory.
        global _gc
        if _gc is None:
            from zmq.utils.garbage import gc as _gc

        hint: pointer(_zhint) = cast(pointer(_zhint), malloc(sizeof(_zhint)))
        hint.id = _gc.store(data, self.tracker_event)
        if not _gc._push_mutex:
            hint.mutex = mutex_allocate()
            _gc._push_mutex = cast(size_t, hint.mutex)
        else:
            hint.mutex = cast(pointer(mutex_t), cast(size_t, _gc._push_mutex))
        hint.sock = cast(p_void, cast(size_t, _gc._push_socket.underlying))

        rc = zmq_msg_init_data(
            zmq_msg_ptr,
            cast(p_void, data_c),
            data_len_c,
            cast(pointer(zmq_free_fn), free_python_msg),
            cast(p_void, hint),
        )
        if rc != 0:
            free(hint)
            _check_rc(rc)
        self._failed_init = False

    def __del__(self):
        if self._failed_init:
            return
        # This simply decreases the 0MQ ref-count of zmq_msg.
        with nogil:
            rc: C.int = zmq_msg_close(address(self.zmq_msg))
        _check_rc(rc)

    def __copy__(self):
        return self.fast_copy()

    def fast_copy(self) -> Frame:
        new_msg: Frame = Frame()
        # This does not copy the contents, but just increases the ref-count
        # of the zmq_msg by one.
        zmq_msg_copy(address(new_msg.zmq_msg), address(self.zmq_msg))
        # Copy the ref to data so the copy won't create a copy when str is
        # called.
        if self._data is not None:
            new_msg._data = self._data
        if self._buffer is not None:
            new_msg._buffer = self._buffer
        if self._bytes is not None:
            new_msg._bytes = self._bytes

        # Frame copies share the tracker and tracker_event
        new_msg.tracker_event = self.tracker_event
        new_msg.tracker = self.tracker

        return new_msg

    # buffer interface code adapted from petsc4py by Lisandro Dalcin, a BSD project

    def __getbuffer__(self, buffer: pointer(Py_buffer), flags: C.int):  # noqa: F821
        # new-style (memoryview) buffer interface
        buffer.buf = zmq_msg_data(address(self.zmq_msg))
        buffer.len = zmq_msg_size(address(self.zmq_msg))

        buffer.obj = self
        buffer.readonly = 0
        buffer.format = "B"
        buffer.ndim = 1
        buffer.shape = address(buffer.len)
        buffer.strides = NULL
        buffer.suboffsets = NULL
        buffer.itemsize = 1
        buffer.internal = NULL

    def __len__(self) -> size_t:
        """Return the length of the message in bytes."""
        sz: size_t = zmq_msg_size(address(self.zmq_msg))
        return sz

    @property
    def buffer(self):
        """A memoryview of the message contents."""
        _buffer = self._buffer and self._buffer()
        if _buffer is not None:
            return _buffer
        _buffer = memoryview(self)
        self._buffer = ref(_buffer)
        return _buffer

    @property
    def bytes(self):
        """The message content as a Python bytes object.

        The first time this property is accessed, a copy of the message
        contents is made. From then on that same copy of the message is
        returned.
        """
        if self._bytes is None:
            self._bytes = _copy_zmq_msg_bytes(address(self.zmq_msg))
        return self._bytes

    def get(self, option):
        """
        Get a Frame option or property.

        See the 0MQ API documentation for zmq_msg_get and zmq_msg_gets
        for details on specific options.

        .. versionadded:: libzmq-3.2
        .. versionadded:: 13.0

        .. versionchanged:: 14.3
            add support for zmq_msg_gets (requires libzmq-4.1)
            All message properties are strings.

        .. versionchanged:: 17.0
            Added support for `routing_id` and `group`.
            Only available if draft API is enabled
            with libzmq >= 4.2.
        """
        rc: C.int = 0
        property_c: p_char = NULL

        # zmq_msg_get
        if isinstance(option, int):
            rc = zmq_msg_get(address(self.zmq_msg), option)
            _check_rc(rc)
            return rc

        if option == 'routing_id':
            routing_id: uint32_t = zmq_msg_routing_id(address(self.zmq_msg))
            if routing_id == 0:
                _check_rc(-1)
            return routing_id
        elif option == 'group':
            buf = zmq_msg_group(address(self.zmq_msg))
            if buf == NULL:
                _check_rc(-1)
            return buf.decode('utf8')

        # zmq_msg_gets
        _check_version((4, 1), "get string properties")
        if isinstance(option, str):
            option = option.encode('utf8')

        if not isinstance(option, bytes):
            raise TypeError(f"expected str, got: {option!r}")

        property_c = option

        result: p_char = cast(p_char, zmq_msg_gets(address(self.zmq_msg), property_c))
        if result == NULL:
            _check_rc(-1)
        return result.decode('utf8')

    def set(self, option, value):
        """Set a Frame option.

        See the 0MQ API documentation for zmq_msg_set
        for details on specific options.

        .. versionadded:: libzmq-3.2
        .. versionadded:: 13.0
        .. versionchanged:: 17.0
            Added support for `routing_id` and `group`.
            Only available if draft API is enabled
            with libzmq >= 4.2.
        """
        rc: C.int

        if option == 'routing_id':
            routing_id: uint32_t = value
            rc = zmq_msg_set_routing_id(address(self.zmq_msg), routing_id)
            _check_rc(rc)
            return
        elif option == 'group':
            if isinstance(value, str):
                value = value.encode('utf8')
            rc = zmq_msg_set_group(address(self.zmq_msg), value)
            _check_rc(rc)
            return

        rc = zmq_msg_set(address(self.zmq_msg), option, value)
        _check_rc(rc)


@cclass
class Context:
    """
    Manage the lifecycle of a 0MQ context.

    Parameters
    ----------
    io_threads : int
        The number of IO threads.
    """

    def __init__(self, io_threads: C.int = 1, shadow: size_t = 0):
        self.handle = NULL
        self._pid = 0
        self._shadow = False

        if shadow:
            self.handle = cast(p_void, shadow)
            self._shadow = True
        else:
            self._shadow = False
            if ZMQ_VERSION_MAJOR >= 3:
                self.handle = zmq_ctx_new()
            else:
                self.handle = zmq_init(io_threads)

        if self.handle == NULL:
            raise ZMQError()

        rc: C.int = 0
        if ZMQ_VERSION_MAJOR >= 3 and not self._shadow:
            rc = zmq_ctx_set(self.handle, ZMQ_IO_THREADS, io_threads)
            _check_rc(rc)

        self.closed = False
        self._pid = getpid()

    @property
    def underlying(self):
        """The address of the underlying libzmq context"""
        return cast(size_t, self.handle)

    @cfunc
    @inline
    def _term(self) -> C.int:
        rc: C.int = 0
        if self.handle != NULL and not self.closed and getpid() == self._pid:
            with nogil:
                rc = zmq_ctx_destroy(self.handle)
        self.handle = NULL
        return rc

    def term(self):
        """
        Close or terminate the context.

        This can be called to close the context by hand. If this is not called,
        the context will automatically be closed when it is garbage collected.
        """
        rc: C.int = self._term()
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            # ignore interrupted term
            # see PEP 475 notes about close & EINTR for why
            pass

        self.closed = True

    def set(self, option: C.int, optval):
        """
        Set a context option.

        See the 0MQ API documentation for zmq_ctx_set
        for details on specific options.

        .. versionadded:: libzmq-3.2
        .. versionadded:: 13.0

        Parameters
        ----------
        option : int
            The option to set.  Available values will depend on your
            version of libzmq.  Examples include::

                zmq.IO_THREADS, zmq.MAX_SOCKETS

        optval : int
            The value of the option to set.
        """
        optval_int_c: C.int
        rc: C.int

        if self.closed:
            raise RuntimeError("Context has been destroyed")

        if not isinstance(optval, int):
            raise TypeError(f'expected int, got: {optval!r}')
        optval_int_c = optval
        rc = zmq_ctx_set(self.handle, option, optval_int_c)
        _check_rc(rc)

    def get(self, option: C.int):
        """
        Get the value of a context option.

        See the 0MQ API documentation for zmq_ctx_get
        for details on specific options.

        .. versionadded:: libzmq-3.2
        .. versionadded:: 13.0

        Parameters
        ----------
        option : int
            The option to get.  Available values will depend on your
            version of libzmq.  Examples include::

                zmq.IO_THREADS, zmq.MAX_SOCKETS

        Returns
        -------
        optval : int
            The value of the option as an integer.
        """
        rc: C.int

        if self.closed:
            raise RuntimeError("Context has been destroyed")

        rc = zmq_ctx_get(self.handle, option)
        _check_rc(rc, error_without_errno=False)
        return rc


@cclass
class Socket:
    """
    A 0MQ socket.

    These objects will generally be constructed via the socket() method of a Context object.

    Note: 0MQ Sockets are *not* threadsafe. **DO NOT** share them across threads.

    Parameters
    ----------
    context : Context
        The 0MQ Context this Socket belongs to.
    socket_type : int
        The socket type, which can be any of the 0MQ socket types:
        REQ, REP, PUB, SUB, PAIR, DEALER, ROUTER, PULL, PUSH, XPUB, XSUB.

    See Also
    --------
    .Context.socket : method for creating a socket bound to a Context.
    """

    def __init__(
        self,
        context=None,
        socket_type: C.int = -1,
        shadow: size_t = 0,
        copy_threshold=None,
    ):
        # pre-init
        self.handle = NULL
        self._pid = 0
        self._shadow = False
        self.context = None

        if copy_threshold is None:
            copy_threshold = zmq.COPY_THRESHOLD
        self.copy_threshold = copy_threshold

        self.handle = NULL
        self.context = context
        if shadow:
            self._shadow = True
            self.handle = cast(p_void, shadow)
        else:
            if context is None:
                raise TypeError("context must be specified")
            if socket_type < 0:
                raise TypeError("socket_type must be specified")
            self._shadow = False
            self.handle = zmq_socket(self.context.handle, socket_type)
        if self.handle == NULL:
            raise ZMQError()
        self._closed = False
        self._pid = getpid()

    @property
    def underlying(self):
        """The address of the underlying libzmq socket"""
        return cast(size_t, self.handle)

    @property
    def closed(self):
        """Whether the socket is closed"""
        return _check_closed_deep(self)

    def close(self, linger=None):
        """
        Close the socket.

        If linger is specified, LINGER sockopt will be set prior to closing.

        This can be called to close the socket by hand. If this is not
        called, the socket will automatically be closed when it is
        garbage collected.
        """
        rc: C.int = 0
        linger_c: C.int
        setlinger: bint = False

        if linger is not None:
            linger_c = linger
            setlinger = True

        if self.handle != NULL and not self._closed and getpid() == self._pid:
            if setlinger:
                zmq_setsockopt(self.handle, ZMQ_LINGER, address(linger_c), sizeof(int))
            rc = zmq_close(self.handle)
            if rc < 0 and zmq_errno() != ENOTSOCK:
                # ignore ENOTSOCK (closed by Context)
                _check_rc(rc)
            self._closed = True
            self.handle = NULL

    def set(self, option: C.int, optval):
        """
        Set socket options.

        See the 0MQ API documentation for details on specific options.

        Parameters
        ----------
        option : int
            The option to set.  Available values will depend on your
            version of libzmq.  Examples include::

                zmq.SUBSCRIBE, UNSUBSCRIBE, IDENTITY, HWM, LINGER, FD

        optval : int or bytes
            The value of the option to set.

        Notes
        -----
        .. warning::

            All options other than zmq.SUBSCRIBE, zmq.UNSUBSCRIBE and
            zmq.LINGER only take effect for subsequent socket bind/connects.
        """
        optval_int64_c: int64_t
        optval_int_c: C.int
        optval_c: p_char
        sz: Py_ssize_t

        _check_closed(self)
        if isinstance(optval, str):
            raise TypeError("unicode not allowed, use setsockopt_string")

        try:
            sopt = SocketOption(option)
        except ValueError:
            # unrecognized option,
            # assume from the future,
            # let EINVAL raise
            opt_type = _OptType.int
        else:
            opt_type = sopt._opt_type

        if opt_type == _OptType.bytes:
            if not isinstance(optval, bytes):
                raise TypeError(f'expected bytes, got: {optval!r}')
            optval_c = PyBytes_AsString(optval)
            sz = PyBytes_Size(optval)
            _setsockopt(self.handle, option, optval_c, sz)
        elif opt_type == _OptType.int64:
            if not isinstance(optval, int):
                raise TypeError(f'expected int, got: {optval!r}')
            optval_int64_c = optval
            _setsockopt(self.handle, option, address(optval_int64_c), sizeof(int64_t))
        else:
            # default is to assume int, which is what most new sockopts will be
            # this lets pyzmq work with newer libzmq which may add constants
            # pyzmq has not yet added, rather than artificially raising. Invalid
            # sockopts will still raise just the same, but it will be libzmq doing
            # the raising.
            if not isinstance(optval, int):
                raise TypeError(f'expected int, got: {optval!r}')
            optval_int_c = optval
            _setsockopt(self.handle, option, address(optval_int_c), sizeof(int))

    def get(self, option: C.int):
        """
        Get the value of a socket option.

        See the 0MQ API documentation for details on specific options.

        Parameters
        ----------
        option : int
            The option to get.  Available values will depend on your
            version of libzmq.  Examples include::

                zmq.IDENTITY, HWM, LINGER, FD, EVENTS

        Returns
        -------
        optval : int or bytes
            The value of the option as a bytestring or int.
        """
        optval_int64_c = declare(int64_t)
        optval_int_c = declare(C.int)
        optval_fd_c = declare(fd_t)
        identity_str_c = declare(char[255])
        sz: size_t

        _check_closed(self)

        try:
            sopt = SocketOption(option)
        except ValueError:
            # unrecognized option,
            # assume from the future,
            # let EINVAL raise
            opt_type = _OptType.int
        else:
            opt_type = sopt._opt_type

        if opt_type == _OptType.bytes:
            sz = 255
            _getsockopt(self.handle, option, cast(p_void, identity_str_c), address(sz))
            # strip null-terminated strings *except* identity
            if (
                option != ZMQ_IDENTITY
                and sz > 0
                and (cast(p_char, identity_str_c))[sz - 1] == b'\0'
            ):
                sz -= 1
            result = PyBytes_FromStringAndSize(cast(p_char, identity_str_c), sz)
        elif opt_type == _OptType.int64:
            sz = sizeof(int64_t)
            _getsockopt(
                self.handle, option, cast(p_void, address(optval_int64_c)), address(sz)
            )
            result = optval_int64_c
        elif opt_type == _OptType.fd:
            sz = sizeof(fd_t)
            _getsockopt(
                self.handle, option, cast(p_void, address(optval_fd_c)), address(sz)
            )
            result = optval_fd_c
        else:
            # default is to assume int, which is what most new sockopts will be
            # this lets pyzmq work with newer libzmq which may add constants
            # pyzmq has not yet added, rather than artificially raising. Invalid
            # sockopts will still raise just the same, but it will be libzmq doing
            # the raising.
            sz = sizeof(int)
            _getsockopt(
                self.handle, option, cast(p_void, address(optval_int_c)), address(sz)
            )
            result = optval_int_c

        return result

    def bind(self, addr):
        """
        Bind the socket to an address.

        This causes the socket to listen on a network port. Sockets on the
        other side of this connection will use ``Socket.connect(addr)`` to
        connect to this socket.

        Parameters
        ----------
        addr : str
            The address string. This has the form 'protocol://interface:port',
            for example 'tcp://127.0.0.1:5555'. Protocols supported include
            tcp, udp, pgm, epgm, inproc and ipc. If the address is unicode, it is
            encoded to utf-8 first.
        """
        rc: C.int
        c_addr: p_char

        _check_closed(self)
        addr_b = addr
        if isinstance(addr, str):
            addr_b = addr.encode('utf-8')
        elif isinstance(addr_b, bytes):
            addr = addr_b.decode('utf-8')

        if not isinstance(addr_b, bytes):
            raise TypeError(f'expected str, got: {addr!r}')
        c_addr = addr_b
        rc = zmq_bind(self.handle, c_addr)
        if rc != 0:
            if IPC_PATH_MAX_LEN and zmq_errno() == ENAMETOOLONG:
                path = addr.split('://', 1)[-1]
                msg = (
                    f'ipc path "{path}" is longer than {IPC_PATH_MAX_LEN} '
                    'characters (sizeof(sockaddr_un.sun_path)). '
                    'zmq.IPC_PATH_MAX_LEN constant can be used '
                    'to check addr length (if it is defined).'
                )
                raise ZMQError(msg=msg)
            elif zmq_errno() == ENOENT:
                path = addr.split('://', 1)[-1]
                msg = f'No such file or directory for ipc path "{path}".'
                raise ZMQError(msg=msg)
        while True:
            try:
                _check_rc(rc)
            except InterruptedSystemCall:
                rc = zmq_bind(self.handle, c_addr)
                continue
            else:
                break

    def connect(self, addr):
        """
        Connect to a remote 0MQ socket.

        Parameters
        ----------
        addr : str
            The address string. This has the form 'protocol://interface:port',
            for example 'tcp://127.0.0.1:5555'. Protocols supported are
            tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
            encoded to utf-8 first.
        """
        rc: C.int
        c_addr: p_char

        _check_closed(self)
        if isinstance(addr, str):
            addr = addr.encode('utf-8')
        if not isinstance(addr, bytes):
            raise TypeError(f'expected str, got: {addr!r}')
        c_addr = addr

        while True:
            try:
                rc = zmq_connect(self.handle, c_addr)
                _check_rc(rc)
            except InterruptedSystemCall:
                # retry syscall
                continue
            else:
                break

    def unbind(self, addr):
        """
        Unbind from an address (undoes a call to bind).

        .. versionadded:: libzmq-3.2
        .. versionadded:: 13.0

        Parameters
        ----------
        addr : str
            The address string. This has the form 'protocol://interface:port',
            for example 'tcp://127.0.0.1:5555'. Protocols supported are
            tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
            encoded to utf-8 first.
        """
        rc: C.int
        c_addr: p_char

        _check_version((3, 2), "unbind")
        _check_closed(self)
        if isinstance(addr, str):
            addr = addr.encode('utf-8')
        if not isinstance(addr, bytes):
            raise TypeError(f'expected str, got: {addr!r}')
        c_addr = addr

        rc = zmq_unbind(self.handle, c_addr)
        if rc != 0:
            raise ZMQError()

    def disconnect(self, addr):
        """
        Disconnect from a remote 0MQ socket (undoes a call to connect).

        .. versionadded:: libzmq-3.2
        .. versionadded:: 13.0

        Parameters
        ----------
        addr : str
            The address string. This has the form 'protocol://interface:port',
            for example 'tcp://127.0.0.1:5555'. Protocols supported are
            tcp, udp, pgm, inproc and ipc. If the address is unicode, it is
            encoded to utf-8 first.
        """
        rc: C.int
        c_addr: p_char

        _check_version((3, 2), "disconnect")
        _check_closed(self)
        if isinstance(addr, str):
            addr = addr.encode('utf-8')
        if not isinstance(addr, bytes):
            raise TypeError(f'expected str, got: {addr!r}')
        c_addr = addr

        rc = zmq_disconnect(self.handle, c_addr)
        if rc != 0:
            raise ZMQError()

    def monitor(self, addr, events: C.int = ZMQ_EVENT_ALL):
        """
        Start publishing socket events on inproc.
        See libzmq docs for zmq_monitor for details.

        While this function is available from libzmq 3.2,
        pyzmq cannot parse monitor messages from libzmq prior to 4.0.

        .. versionadded: libzmq-3.2
        .. versionadded: 14.0

        Parameters
        ----------
        addr : str
            The inproc url used for monitoring. Passing None as
            the addr will cause an existing socket monitor to be
            deregistered.
        events : int
            default: zmq.EVENT_ALL
            The zmq event bitmask for which events will be sent to the monitor.
        """
        _check_version((3, 2), "monitor")

        if isinstance(addr, str):
            # cast str to utf8 bytes
            addr = addr.encode("utf-8")

        # cast bytes to char*
        c_addr: p_char

        if addr is None:
            c_addr = NULL
        else:
            # let Cython do the casting,
            # but return a nicer error message if it fails
            try:
                c_addr = addr
            except TypeError:
                raise TypeError(f"Monitor addr must be str, got {addr!r}") from None

        _check_rc(zmq_socket_monitor(self.handle, c_addr, events))

    def join(self, group):
        """
        Join a RADIO-DISH group

        Only for DISH sockets.

        libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API

        .. versionadded:: 17
        """
        _check_version((4, 2), "RADIO-DISH")
        if not zmq.has('draft'):
            raise RuntimeError("libzmq must be built with draft support")
        if isinstance(group, str):
            group = group.encode('utf8')
        rc: C.int = zmq_join(self.handle, group)
        _check_rc(rc)

    def leave(self, group):
        """
        Leave a RADIO-DISH group

        Only for DISH sockets.

        libzmq and pyzmq must have been built with ZMQ_BUILD_DRAFT_API

        .. versionadded:: 17
        """
        _check_version((4, 2), "RADIO-DISH")
        if not zmq.has('draft'):
            raise RuntimeError("libzmq must be built with draft support")
        rc: C.int = zmq_leave(self.handle, group)
        _check_rc(rc)

    def send(self, data, flags=0, copy: bint = True, track: bint = False):
        """
        Send a single zmq message frame on this socket.

        This queues the message to be sent by the IO thread at a later time.

        With flags=NOBLOCK, this raises :class:`ZMQError` if the queue is full;
        otherwise, this waits until space is available.
        See :class:`Poller` for more general non-blocking I/O.

        Parameters
        ----------
        data : bytes, Frame, memoryview
            The content of the message. This can be any object that provides
            the Python buffer API (`memoryview(data)` can be called).
        flags : int
            0, NOBLOCK, SNDMORE, or NOBLOCK|SNDMORE.
        copy : bool
            Should the message be sent in a copying or non-copying manner.
        track : bool
            Should the message be tracked for notification that ZMQ has
            finished with it? (ignored if copy=True)

        Returns
        -------
        None : if `copy` or not track
            None if message was sent, raises an exception otherwise.
        MessageTracker : if track and not copy
            a MessageTracker object, whose `done` property will
            be False until the send is completed.

        Raises
        ------
        TypeError
            If a unicode object is passed
        ValueError
            If `track=True`, but an untracked Frame is passed.
        ZMQError
            for any of the reasons zmq_msg_send might fail (including
            if NOBLOCK is set and the outgoing queue is full).

        """
        _check_closed(self)

        if isinstance(data, str):
            raise TypeError("unicode not allowed, use send_string")

        if copy and not isinstance(data, Frame):
            return _send_copy(self.handle, data, flags)
        else:
            if isinstance(data, Frame):
                if track and not data.tracker:
                    raise ValueError('Not a tracked message')
                msg = data
            else:
                if self.copy_threshold:
                    buf = memoryview(data)
                    # always copy messages smaller than copy_threshold
                    if buf.nbytes < self.copy_threshold:
                        _send_copy(self.handle, buf, flags)
                        return zmq._FINISHED_TRACKER
                msg = Frame(data, track=track, copy_threshold=self.copy_threshold)
            return _send_frame(self.handle, msg, flags)

    def recv(self, flags=0, copy: bint = True, track: bint = False):
        """
        Receive a message.

        With flags=NOBLOCK, this raises :class:`ZMQError` if no messages have
        arrived; otherwise, this waits until a message arrives.
        See :class:`Poller` for more general non-blocking I/O.

        Parameters
        ----------
        flags : int
            0 or NOBLOCK.
        copy : bool
            Should the message be received in a copying or non-copying manner?
            If False a Frame object is returned, if True a string copy of
            message is returned.
        track : bool
            Should the message be tracked for notification that ZMQ has
            finished with it? (ignored if copy=True)

        Returns
        -------
        msg : bytes or Frame
            The received message frame.  If `copy` is False, then it will be a Frame,
            otherwise it will be bytes.

        Raises
        ------
        ZMQError
            for any of the reasons zmq_msg_recv might fail (including if
            NOBLOCK is set and no new messages have arrived).
        """
        _check_closed(self)

        if copy:
            return _recv_copy(self.handle, flags)
        else:
            frame = _recv_frame(self.handle, flags, track)
            frame.more = self.get(zmq.RCVMORE)
            return frame


# inline socket methods


@inline
@cfunc
def _check_closed(s: Socket):
    """raise ENOTSUP if socket is closed

    Does not do a deep check
    """
    if s._closed:
        raise ZMQError(ENOTSOCK)


@inline
@cfunc
def _check_closed_deep(s: Socket) -> bint:
    """thorough check of whether the socket has been closed,
    even if by another entity (e.g. ctx.destroy).

    Only used by the `closed` property.

    returns True if closed, False otherwise
    """
    rc: C.int
    errno: C.int
    stype = declare(C.int)
    sz: size_t = sizeof(int)

    if s._closed:
        return True
    else:
        rc = zmq_getsockopt(
            s.handle, ZMQ_TYPE, cast(p_void, address(stype)), address(sz)
        )
        if rc < 0:
            errno = zmq_errno()
            if errno == ENOTSOCK:
                s._closed = True
                return True
            elif errno == ZMQ_ETERM:
                # don't raise ETERM when checking if we're closed
                return False
        else:
            _check_rc(rc)
    return False


@cfunc
@inline
def _recv_frame(handle: p_void, flags: C.int = 0, track: bint = False) -> Frame:
    """Receive a message in a non-copying manner and return a Frame."""
    rc: C.int
    msg = zmq.Frame(track=track)
    cmsg: Frame = msg

    while True:
        with nogil:
            rc = zmq_msg_recv(address(cmsg.zmq_msg), handle, flags)
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        else:
            break
    return msg


@cfunc
@inline
def _recv_copy(handle: p_void, flags: C.int = 0):
    """Receive a message and return a copy"""
    zmq_msg = declare(zmq_msg_t)
    zmq_msg_p: pointer(zmq_msg_t) = address(zmq_msg)
    rc: C.int = zmq_msg_init(zmq_msg_p)
    _check_rc(rc)
    while True:
        with nogil:
            rc = zmq_msg_recv(zmq_msg_p, handle, flags)
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        except Exception:
            zmq_msg_close(zmq_msg_p)  # ensure msg is closed on failure
            raise
        else:
            break

    msg_bytes = _copy_zmq_msg_bytes(zmq_msg_p)
    zmq_msg_close(zmq_msg_p)
    return msg_bytes


@cfunc
@inline
def _send_frame(handle: p_void, msg: Frame, flags: C.int = 0):
    """Send a Frame on this socket in a non-copy manner."""
    rc: C.int
    msg_copy: Frame

    # Always copy so the original message isn't garbage collected.
    # This doesn't do a real copy, just a reference.
    msg_copy = msg.fast_copy()

    while True:
        with nogil:
            rc = zmq_msg_send(address(msg_copy.zmq_msg), handle, flags)
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        else:
            break

    return msg.tracker


@cfunc
@inline
def _send_copy(handle: p_void, buf, flags: C.int = 0):
    """Send a message on this socket by copying its content."""
    rc: C.int
    msg = declare(zmq_msg_t)
    c_bytes = declare(p_char)
    c_bytes_len: Py_ssize_t = 0

    # copy to c array:
    asbuffer_r(buf, cast(pointer(p_void), address(c_bytes)), address(c_bytes_len))

    # Copy the msg before sending. This avoids any complications with
    # the GIL, etc.
    # If zmq_msg_init_* fails we must not call zmq_msg_close (Bus Error)
    rc = zmq_msg_init_size(address(msg), c_bytes_len)
    _check_rc(rc)

    while True:
        with nogil:
            memcpy(zmq_msg_data(address(msg)), c_bytes, zmq_msg_size(address(msg)))
            rc = zmq_msg_send(address(msg), handle, flags)
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        except Exception:
            zmq_msg_close(address(msg))  # close the unused msg
            raise  # raise original exception
        else:
            rc = zmq_msg_close(address(msg))
            _check_rc(rc)
            break


@cfunc
@inline
def _getsockopt(handle: p_void, option: C.int, optval: p_void, sz: pointer(size_t)):
    """getsockopt, retrying interrupted calls

    checks rc, raising ZMQError on failure.
    """
    rc: C.int = 0
    while True:
        rc = zmq_getsockopt(handle, option, optval, sz)
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        else:
            break


@cfunc
@inline
def _setsockopt(handle: p_void, option: C.int, optval: p_void, sz: size_t):
    """setsockopt, retrying interrupted calls

    checks rc, raising ZMQError on failure.
    """
    rc: C.int = 0
    while True:
        rc = zmq_setsockopt(handle, option, optval, sz)
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        else:
            break


# General utility functions


def zmq_errno():
    """Return the integer errno of the most recent zmq error."""
    return _zmq_errno()


def strerror(errno: C.int) -> str:
    """
    Return the error string given the error number.
    """
    str_e: bytes = zmq_strerror(errno)
    return str_e.decode("utf8", "replace")


def zmq_version_info() -> tuple[int, int, int]:
    """Return the version of ZeroMQ itself as a 3-tuple of ints."""
    major: C.int = 0
    minor: C.int = 0
    patch: C.int = 0
    _zmq_version(address(major), address(minor), address(patch))
    return (major, minor, patch)


def has(capability) -> bool:
    """Check for zmq capability by name (e.g. 'ipc', 'curve')

    .. versionadded:: libzmq-4.1
    .. versionadded:: 14.1
    """
    _check_version((4, 1), 'zmq.has')
    ccap: bytes
    if isinstance(capability, str):
        capability = capability.encode('utf8')
    ccap = capability
    return bool(zmq_has(ccap))


def curve_keypair() -> tuple[bytes, bytes]:
    """generate a Z85 key pair for use with zmq.CURVE security

    Requires libzmq (≥ 4.0) to have been built with CURVE support.

    .. versionadded:: libzmq-4.0
    .. versionadded:: 14.0

    Returns
    -------
    public: bytes
        The public key as 40 byte z85-encoded bytestring.
    private: bytes
        The private key as 40 byte z85-encoded bytestring.
    """
    rc: C.int
    public_key = declare(char[64])
    secret_key = declare(char[64])
    _check_version((4, 0), "curve_keypair")
    # see huge comment in libzmq/src/random.cpp
    # about threadsafety of random initialization
    rc = zmq_curve_keypair(public_key, secret_key)
    _check_rc(rc)
    return public_key, secret_key


def curve_public(secret_key) -> bytes:
    """Compute the public key corresponding to a secret key for use
    with zmq.CURVE security

    Requires libzmq (≥ 4.2) to have been built with CURVE support.

    Parameters
    ----------
    private
        The private key as a 40 byte z85-encoded bytestring

    Returns
    -------
    bytes
        The public key as a 40 byte z85-encoded bytestring
    """
    if isinstance(secret_key, str):
        secret_key = secret_key.encode('utf8')
    if not len(secret_key) == 40:
        raise ValueError('secret key must be a 40 byte z85 encoded string')

    rc: C.int
    public_key = declare(char[64])
    c_secret_key: pointer(char) = secret_key
    _check_version((4, 2), "curve_public")
    # see huge comment in libzmq/src/random.cpp
    # about threadsafety of random initialization
    rc = zmq_curve_public(public_key, c_secret_key)
    _check_rc(rc)
    return public_key[:40]


# polling
def zmq_poll(sockets, timeout: C.int = -1):
    """zmq_poll(sockets, timeout=-1)

    Poll a set of 0MQ sockets, native file descs. or sockets.

    Parameters
    ----------
    sockets : list of tuples of (socket, flags)
        Each element of this list is a two-tuple containing a socket
        and a flags. The socket may be a 0MQ socket or any object with
        a ``fileno()`` method. The flags can be zmq.POLLIN (for detecting
        for incoming messages), zmq.POLLOUT (for detecting that send is OK)
        or zmq.POLLIN|zmq.POLLOUT for detecting both.
    timeout : int
        The number of milliseconds to poll for. Negative means no timeout.
    """
    rc: C.int
    i: C.int
    pollitems: pointer(zmq_pollitem_t) = NULL
    nsockets: C.int = len(sockets)

    if nsockets == 0:
        return []

    pollitems = cast(pointer(zmq_pollitem_t), malloc(nsockets * sizeof(zmq_pollitem_t)))
    if pollitems == NULL:
        raise MemoryError("Could not allocate poll items")

    if ZMQ_VERSION_MAJOR < 3:
        # timeout is us in 2.x, ms in 3.x
        # expected input is ms (matches 3.x)
        timeout = 1000 * timeout

    for i in range(nsockets):
        s, events = sockets[i]
        if isinstance(s, Socket):
            pollitems[i].socket = cast(Socket, s).handle
            pollitems[i].fd = 0
            pollitems[i].events = events
            pollitems[i].revents = 0
        elif isinstance(s, int):
            pollitems[i].socket = NULL
            pollitems[i].fd = s
            pollitems[i].events = events
            pollitems[i].revents = 0
        elif hasattr(s, 'fileno'):
            try:
                fileno = int(s.fileno())
            except Exception:
                free(pollitems)
                raise ValueError('fileno() must return a valid integer fd')
            else:
                pollitems[i].socket = NULL
                pollitems[i].fd = fileno
                pollitems[i].events = events
                pollitems[i].revents = 0
        else:
            free(pollitems)
            raise TypeError(
                "Socket must be a 0MQ socket, an integer fd or have "
                f"a fileno() method: {s!r}"
            )

    ms_passed: int = 0
    try:
        while True:
            start = time.monotonic()
            with nogil:
                rc = zmq_poll_c(pollitems, nsockets, timeout)
            try:
                _check_rc(rc)
            except InterruptedSystemCall:
                if timeout > 0:
                    ms_passed = int(1000 * (time.monotonic() - start))
                    if ms_passed < 0:
                        # don't allow negative ms_passed,
                        # which can happen on old Python versions without time.monotonic.
                        warnings.warn(
                            f"Negative elapsed time for interrupted poll: {ms_passed}."
                            "  Did the clock change?",
                            RuntimeWarning,
                        )
                        # treat this case the same as no time passing,
                        # since it should be rare and not happen twice in a row.
                        ms_passed = 0
                    timeout = max(0, timeout - ms_passed)
                continue
            else:
                break
    except Exception:
        free(pollitems)
        raise

    results = []
    for i in range(nsockets):
        revents = pollitems[i].revents
        # for compatibility with select.poll:
        # - only return sockets with non-zero status
        # - return the fd for plain sockets
        if revents > 0:
            if pollitems[i].socket != NULL:
                s = sockets[i][0]
            else:
                s = pollitems[i].fd
            results.append((s, revents))

    free(pollitems)
    return results


# device functions


def device(device_type: C.int, frontend: Socket, backend: Socket = None):
    """
    Start a zeromq device.

    .. deprecated:: libzmq-3.2
        Use zmq.proxy

    Parameters
    ----------
    device_type : int
        one of: QUEUE, FORWARDER, STREAMER
        The type of device to start.
    frontend : Socket
        The Socket instance for the incoming traffic.
    backend : Socket
        The Socket instance for the outbound traffic.
    """
    if ZMQ_VERSION_MAJOR >= 3:
        return proxy(frontend, backend)

    rc: C.int = 0
    while True:
        with nogil:
            rc = zmq_device(device_type, frontend.handle, backend.handle)
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        else:
            break
    return rc


def proxy(frontend: Socket, backend: Socket, capture: Socket = None):
    """
    Start a zeromq proxy (replacement for device).

    .. versionadded:: libzmq-3.2
    .. versionadded:: 13.0

    Parameters
    ----------
    frontend : Socket
        The Socket instance for the incoming traffic.
    backend : Socket
        The Socket instance for the outbound traffic.
    capture : Socket (optional)
        The Socket instance for capturing traffic.
    """
    rc: C.int = 0
    capture_handle: p_void
    if isinstance(capture, Socket):
        capture_handle = capture.handle
    else:
        capture_handle = NULL
    while True:
        with nogil:
            rc = zmq_proxy(frontend.handle, backend.handle, capture_handle)
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        else:
            break
    return rc


def proxy_steerable(
    frontend: Socket,
    backend: Socket,
    capture: Socket = None,
    control: Socket = None,
):
    """
    Start a zeromq proxy with control flow.

    .. versionadded:: libzmq-4.1
    .. versionadded:: 18.0

    Parameters
    ----------
    frontend : Socket
        The Socket instance for the incoming traffic.
    backend : Socket
        The Socket instance for the outbound traffic.
    capture : Socket (optional)
        The Socket instance for capturing traffic.
    control : Socket (optional)
        The Socket instance for control flow.
    """
    rc: C.int = 0
    capture_handle: p_void
    if isinstance(capture, Socket):
        capture_handle = capture.handle
    else:
        capture_handle = NULL
    if isinstance(control, Socket):
        control_handle = control.handle
    else:
        control_handle = NULL
    while True:
        with nogil:
            rc = zmq_proxy_steerable(
                frontend.handle, backend.handle, capture_handle, control_handle
            )
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        else:
            break
    return rc


# monitored queue - like proxy (predates libzmq proxy)
# but supports ROUTER-ROUTER devices
@cfunc
@inline
@nogil
def _mq_relay(
    in_socket: p_void,
    out_socket: p_void,
    side_socket: p_void,
    msg: zmq_msg_t,
    side_msg: zmq_msg_t,
    id_msg: zmq_msg_t,
    swap_ids: bint,
) -> C.int:
    rc: C.int
    flags: C.int
    flagsz = declare(size_t)
    more = declare(int)
    flagsz = sizeof(int)

    if swap_ids:  # both router, must send second identity first
        # recv two ids into msg, id_msg
        rc = zmq_msg_recv(address(msg), in_socket, 0)
        if rc < 0:
            return rc

        rc = zmq_msg_recv(address(id_msg), in_socket, 0)
        if rc < 0:
            return rc

        # send second id (id_msg) first
        # !!!! always send a copy before the original !!!!
        rc = zmq_msg_copy(address(side_msg), address(id_msg))
        if rc < 0:
            return rc
        rc = zmq_msg_send(address(side_msg), out_socket, ZMQ_SNDMORE)
        if rc < 0:
            return rc
        rc = zmq_msg_send(address(id_msg), side_socket, ZMQ_SNDMORE)
        if rc < 0:
            return rc
        # send first id (msg) second
        rc = zmq_msg_copy(address(side_msg), address(msg))
        if rc < 0:
            return rc
        rc = zmq_msg_send(address(side_msg), out_socket, ZMQ_SNDMORE)
        if rc < 0:
            return rc
        rc = zmq_msg_send(address(msg), side_socket, ZMQ_SNDMORE)
        if rc < 0:
            return rc
    while True:
        rc = zmq_msg_recv(address(msg), in_socket, 0)
        if rc < 0:
            return rc
        # assert (rc == 0)
        rc = zmq_getsockopt(in_socket, ZMQ_RCVMORE, address(more), address(flagsz))
        if rc < 0:
            return rc
        flags = 0
        if more:
            flags |= ZMQ_SNDMORE

        rc = zmq_msg_copy(address(side_msg), address(msg))
        if rc < 0:
            return rc
        if flags:
            rc = zmq_msg_send(address(side_msg), out_socket, flags)
            if rc < 0:
                return rc
            # only SNDMORE for side-socket
            rc = zmq_msg_send(address(msg), side_socket, ZMQ_SNDMORE)
            if rc < 0:
                return rc
        else:
            rc = zmq_msg_send(address(side_msg), out_socket, 0)
            if rc < 0:
                return rc
            rc = zmq_msg_send(address(msg), side_socket, 0)
            if rc < 0:
                return rc
            break
    return rc


@cfunc
@inline
@nogil
def _mq_inline(
    in_socket: p_void,
    out_socket: p_void,
    side_socket: p_void,
    in_msg_ptr: pointer(zmq_msg_t),
    out_msg_ptr: pointer(zmq_msg_t),
    swap_ids: bint,
) -> C.int:
    """
    inner C function for monitored_queue
    """

    msg: zmq_msg_t = declare(zmq_msg_t)
    rc: C.int = zmq_msg_init(address(msg))
    id_msg = declare(zmq_msg_t)
    rc = zmq_msg_init(address(id_msg))
    if rc < 0:
        return rc
    side_msg = declare(zmq_msg_t)
    rc = zmq_msg_init(address(side_msg))
    if rc < 0:
        return rc

    items = declare(zmq_pollitem_t[2])
    items[0].socket = in_socket
    items[0].events = ZMQ_POLLIN
    items[0].fd = items[0].revents = 0
    items[1].socket = out_socket
    items[1].events = ZMQ_POLLIN
    items[1].fd = items[1].revents = 0

    while True:
        # wait for the next message to process
        rc = zmq_poll_c(address(items[0]), 2, -1)
        if rc < 0:
            return rc
        if items[0].revents & ZMQ_POLLIN:
            # send in_prefix to side socket
            rc = zmq_msg_copy(address(side_msg), in_msg_ptr)
            if rc < 0:
                return rc
            rc = zmq_msg_send(address(side_msg), side_socket, ZMQ_SNDMORE)
            if rc < 0:
                return rc
            # relay the rest of the message
            rc = _mq_relay(
                in_socket, out_socket, side_socket, msg, side_msg, id_msg, swap_ids
            )
            if rc < 0:
                return rc
        if items[1].revents & ZMQ_POLLIN:
            # send out_prefix to side socket
            rc = zmq_msg_copy(address(side_msg), out_msg_ptr)
            if rc < 0:
                return rc
            rc = zmq_msg_send(address(side_msg), side_socket, ZMQ_SNDMORE)
            if rc < 0:
                return rc
            # relay the rest of the message
            rc = _mq_relay(
                out_socket, in_socket, side_socket, msg, side_msg, id_msg, swap_ids
            )
            if rc < 0:
                return rc
    return rc


def monitored_queue(
    in_socket: Socket,
    out_socket: Socket,
    mon_socket: Socket,
    in_prefix: bytes = b'in',
    out_prefix: bytes = b'out',
):
    """
    Start a monitored queue device.

    A monitored queue is very similar to the zmq.proxy device (monitored queue came first).

    Differences from zmq.proxy:

    - monitored_queue supports both in and out being ROUTER sockets
      (via swapping IDENTITY prefixes).
    - monitor messages are prefixed, making in and out messages distinguishable.

    Parameters
    ----------
    in_socket : zmq.Socket
        One of the sockets to the Queue. Its messages will be prefixed with
        'in'.
    out_socket : zmq.Socket
        One of the sockets to the Queue. Its messages will be prefixed with
        'out'. The only difference between in/out socket is this prefix.
    mon_socket : zmq.Socket
        This socket sends out every message received by each of the others
        with an in/out prefix specifying which one it was.
    in_prefix : str
        Prefix added to broadcast messages from in_socket.
    out_prefix : str
        Prefix added to broadcast messages from out_socket.
    """
    ins: p_void = in_socket.handle
    outs: p_void = out_socket.handle
    mons: p_void = mon_socket.handle
    in_msg = declare(zmq_msg_t)
    out_msg = declare(zmq_msg_t)
    swap_ids: bint
    msg_c: p_char = NULL
    msg_c_len = declare(Py_ssize_t)
    rc: C.int

    # force swap_ids if both ROUTERs
    swap_ids = in_socket.type == ZMQ_ROUTER and out_socket.type == ZMQ_ROUTER

    # build zmq_msg objects from str prefixes
    asbuffer_r(in_prefix, cast(pointer(p_void), address(msg_c)), address(msg_c_len))
    rc = zmq_msg_init_size(address(in_msg), msg_c_len)
    _check_rc(rc)

    memcpy(zmq_msg_data(address(in_msg)), msg_c, zmq_msg_size(address(in_msg)))

    asbuffer_r(out_prefix, cast(pointer(p_void), address(msg_c)), address(msg_c_len))

    rc = zmq_msg_init_size(address(out_msg), msg_c_len)
    _check_rc(rc)

    while True:
        with nogil:
            memcpy(
                zmq_msg_data(address(out_msg)), msg_c, zmq_msg_size(address(out_msg))
            )
            rc = _mq_inline(
                ins, outs, mons, address(in_msg), address(out_msg), swap_ids
            )
        try:
            _check_rc(rc)
        except InterruptedSystemCall:
            continue
        else:
            break
    return rc


__all__ = [
    'IPC_PATH_MAX_LEN',
    'Context',
    'Socket',
    'Frame',
    'has',
    'curve_keypair',
    'curve_public',
    'zmq_version_info',
    'zmq_errno',
    'zmq_poll',
    'strerror',
    'device',
    'proxy',
    'proxy_steerable',
]
