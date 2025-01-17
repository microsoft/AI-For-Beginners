"""zmq Cython backend augmented declarations"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

from zmq.backend.cython.libzmq cimport zmq_msg_t


cdef class Context:

    cdef object __weakref__  # enable weakref
    cdef void *handle  # The C handle for the underlying zmq object.
    cdef bint _shadow  # whether the Context is a shadow wrapper of another
    cdef int _pid  # the pid of the process which created me (for fork safety)

    cdef public bint closed  # bool property for a closed context.
    cdef inline int _term(self)

cdef class MessageTracker(object):
    cdef set events  # Message Event objects to track.
    cdef set peers  # Other Message or MessageTracker objects.

cdef class Frame:

    cdef zmq_msg_t zmq_msg
    cdef object _data      # The actual message data as a Python object.
    cdef object _buffer    # A Python memoryview of the message contents
    cdef object _bytes     # A bytes copy of the message.
    cdef bint _failed_init # flag to hold failed init
    cdef public object tracker_event  # Event for use with zmq_free_fn.
    cdef public object tracker        # MessageTracker object.
    cdef public bint more             # whether RCVMORE was set

    cdef Frame fast_copy(self) # Create shallow copy of Message object.

cdef class Socket:

    cdef object __weakref__     # enable weakref
    cdef void *handle           # The C handle for the underlying zmq object.
    cdef bint _shadow           # whether the Socket is a shadow wrapper of another
    # Hold on to a reference to the context to make sure it is not garbage
    # collected until the socket it done with it.
    cdef public Context context # The zmq Context object that owns this.
    cdef public bint _closed    # bool property for a closed socket.
    cdef public int copy_threshold # threshold below which pyzmq will always copy messages
    cdef int _pid               # the pid of the process which created me (for fork safety)

    # cpdef methods for direct-cython access:
    cpdef object send(self, data, int flags=*, bint copy=*, bint track=*)
    cpdef object recv(self, int flags=*, bint copy=*, bint track=*)
