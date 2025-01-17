from _pydevd_bundle.pydevd_constants import (
    STATE_RUN,
    PYTHON_SUSPEND,
    SUPPORT_GEVENT,
    ForkSafeLock,
    _current_frames,
    STATE_SUSPEND,
    get_global_debugger,
    get_thread_id,
)
from _pydev_bundle import pydev_log
from _pydev_bundle._pydev_saved_modules import threading
from _pydev_bundle.pydev_is_thread_alive import is_thread_alive
import weakref

version = 11


# =======================================================================================================================
# PyDBAdditionalThreadInfo
# =======================================================================================================================
# fmt: off
# IFDEF CYTHON
# cdef class PyDBAdditionalThreadInfo:
# ELSE
class PyDBAdditionalThreadInfo(object):
# ENDIF
# fmt: on

    # Note: the params in cython are declared in pydevd_cython.pxd.
    # fmt: off
    # IFDEF CYTHON
    # ELSE
    __slots__ = [
        "pydev_state",
        "pydev_step_stop",
        "pydev_original_step_cmd",
        "pydev_step_cmd",
        "pydev_notify_kill",
        "pydev_django_resolve_frame",
        "pydev_call_from_jinja2",
        "pydev_call_inside_jinja2",
        "is_tracing",
        "conditional_breakpoint_exception",
        "pydev_message",
        "suspend_type",
        "pydev_next_line",
        "pydev_func_name",
        "suspended_at_unhandled",
        "trace_suspend_type",
        "top_level_thread_tracer_no_back_frames",
        "top_level_thread_tracer_unhandled",
        "thread_tracer",
        "step_in_initial_location",
        # Used for CMD_SMART_STEP_INTO (to know which smart step into variant to use)
        "pydev_smart_parent_offset",
        "pydev_smart_child_offset",
        # Used for CMD_SMART_STEP_INTO (list[_pydevd_bundle.pydevd_bytecode_utils.Variant])
        # Filled when the cmd_get_smart_step_into_variants is requested (so, this is a copy
        # of the last request for a given thread and pydev_smart_parent_offset/pydev_smart_child_offset relies on it).
        "pydev_smart_step_into_variants",
        "target_id_to_smart_step_into_variant",
        "pydev_use_scoped_step_frame",
        "weak_thread",
        "is_in_wait_loop",
    ]
    # ENDIF
    # fmt: on

    def __init__(self):
        self.pydev_state = STATE_RUN  # STATE_RUN or STATE_SUSPEND
        self.pydev_step_stop = None

        # Note: we have `pydev_original_step_cmd` and `pydev_step_cmd` because the original is to
        # say the action that started it and the other is to say what's the current tracing behavior
        # (because it's possible that we start with a step over but may have to switch to a
        # different step strategy -- for instance, if a step over is done and we return the current
        # method the strategy is changed to a step in).

        self.pydev_original_step_cmd = -1  # Something as CMD_STEP_INTO, CMD_STEP_OVER, etc.
        self.pydev_step_cmd = -1  # Something as CMD_STEP_INTO, CMD_STEP_OVER, etc.

        self.pydev_notify_kill = False
        self.pydev_django_resolve_frame = False
        self.pydev_call_from_jinja2 = None
        self.pydev_call_inside_jinja2 = None
        self.is_tracing = 0
        self.conditional_breakpoint_exception = None
        self.pydev_message = ""
        self.suspend_type = PYTHON_SUSPEND
        self.pydev_next_line = -1
        self.pydev_func_name = ".invalid."  # Must match the type in cython
        self.suspended_at_unhandled = False
        self.trace_suspend_type = "trace"  # 'trace' or 'frame_eval'
        self.top_level_thread_tracer_no_back_frames = []
        self.top_level_thread_tracer_unhandled = None
        self.thread_tracer = None
        self.step_in_initial_location = None
        self.pydev_smart_parent_offset = -1
        self.pydev_smart_child_offset = -1
        self.pydev_smart_step_into_variants = ()
        self.target_id_to_smart_step_into_variant = {}

        # Flag to indicate ipython use-case where each line will be executed as a call/line/return
        # in a new new frame but in practice we want to consider each new frame as if it was all
        # part of the same frame.
        #
        # In practice this means that a step over shouldn't revert to a step in and we need some
        # special logic to know when we should stop in a step over as we need to consider 2
        # different frames as being equal if they're logically the continuation of a frame
        # being executed by ipython line by line.
        #
        # See: https://github.com/microsoft/debugpy/issues/869#issuecomment-1132141003
        self.pydev_use_scoped_step_frame = False
        self.weak_thread = None

        # Purpose: detect if this thread is suspended and actually in the wait loop
        # at this time (otherwise it may be suspended but still didn't reach a point.
        # to pause).
        self.is_in_wait_loop = False

    # fmt: off
    # IFDEF CYTHON
    # cpdef object _get_related_thread(self):
    # ELSE
    def _get_related_thread(self):
    # ENDIF
    # fmt: on
        if self.pydev_notify_kill:  # Already killed
            return None

        if self.weak_thread is None:
            return None

        thread = self.weak_thread()
        if thread is None:
            return False

        if not is_thread_alive(thread):
            return None

        if thread._ident is None:  # Can this happen?
            pydev_log.critical("thread._ident is None in _get_related_thread!")
            return None

        if threading._active.get(thread._ident) is not thread:
            return None

        return thread

    # fmt: off
    # IFDEF CYTHON
    # cpdef bint _is_stepping(self):
    # ELSE
    def _is_stepping(self):
    # ENDIF
    # fmt: on
        if self.pydev_state == STATE_RUN and self.pydev_step_cmd != -1:
            # This means actually stepping in a step operation.
            return True

        if self.pydev_state == STATE_SUSPEND and self.is_in_wait_loop:
            # This means stepping because it was suspended but still didn't
            # reach a suspension point.
            return True

        return False

    # fmt: off
    # IFDEF CYTHON
    # cpdef get_topmost_frame(self, thread):
    # ELSE
    def get_topmost_frame(self, thread):
    # ENDIF
    # fmt: on
        """
        Gets the topmost frame for the given thread. Note that it may be None
        and callers should remove the reference to the frame as soon as possible
        to avoid disturbing user code.
        """
        # sys._current_frames(): dictionary with thread id -> topmost frame
        current_frames = _current_frames()
        topmost_frame = current_frames.get(thread._ident)
        if topmost_frame is None:
            # Note: this is expected for dummy threads (so, getting the topmost frame should be
            # treated as optional).
            pydev_log.info(
                "Unable to get topmost frame for thread: %s, thread.ident: %s, id(thread): %s\nCurrent frames: %s.\n" "GEVENT_SUPPORT: %s",
                thread,
                thread.ident,
                id(thread),
                current_frames,
                SUPPORT_GEVENT,
            )

        return topmost_frame

    # fmt: off
    # IFDEF CYTHON
    # cpdef update_stepping_info(self):
    # ELSE
    def update_stepping_info(self):
    # ENDIF
    # fmt: on
        _update_stepping_info(self)

    def __str__(self):
        return "State:%s Stop:%s Cmd: %s Kill:%s" % (self.pydev_state, self.pydev_step_stop, self.pydev_step_cmd, self.pydev_notify_kill)


_set_additional_thread_info_lock = ForkSafeLock()
_next_additional_info = [PyDBAdditionalThreadInfo()]


# fmt: off
# IFDEF CYTHON
# cpdef set_additional_thread_info(thread):
# ELSE
def set_additional_thread_info(thread):
# ENDIF
# fmt: on
    try:
        additional_info = thread.additional_info
        if additional_info is None:
            raise AttributeError()
    except:
        with _set_additional_thread_info_lock:
            # If it's not there, set it within a lock to avoid any racing
            # conditions.
            try:
                additional_info = thread.additional_info
            except:
                additional_info = None

            if additional_info is None:
                # Note: don't call PyDBAdditionalThreadInfo constructor at this
                # point as it can piggy-back into the debugger which could
                # get here again, rather get the global ref which was pre-created
                # and add a new entry only after we set thread.additional_info.
                additional_info = _next_additional_info[0]
                thread.additional_info = additional_info
                additional_info.weak_thread = weakref.ref(thread)
                add_additional_info(additional_info)
                del _next_additional_info[:]
                _next_additional_info.append(PyDBAdditionalThreadInfo())

    return additional_info


# fmt: off
# IFDEF CYTHON
# cdef set _all_infos
# cdef set _infos_stepping
# cdef object _update_infos_lock
# ELSE
# ENDIF
# fmt: on

_all_infos = set()
_infos_stepping = set()
_update_infos_lock = ForkSafeLock()


# fmt: off
# IFDEF CYTHON
# cdef _update_stepping_info(PyDBAdditionalThreadInfo info):
# ELSE
def _update_stepping_info(info):
# ENDIF
# fmt: on

    global _infos_stepping
    global _all_infos

    with _update_infos_lock:
        # Removes entries that are no longer valid.
        new_all_infos = set()
        for info in _all_infos:
            if info._get_related_thread() is not None:
                new_all_infos.add(info)
        _all_infos = new_all_infos

        new_stepping = set()
        for info in _all_infos:
            if info._is_stepping():
                new_stepping.add(info)
        _infos_stepping = new_stepping

    py_db = get_global_debugger()
    if py_db is not None and not py_db.pydb_disposed:
        thread = info.weak_thread()
        if thread is not None:
            thread_id = get_thread_id(thread)
            _queue, event = py_db.get_internal_queue_and_event(thread_id)
            event.set()

# fmt: off
# IFDEF CYTHON
# cpdef add_additional_info(PyDBAdditionalThreadInfo info):
# ELSE
def add_additional_info(info):
# ENDIF
# fmt: on
    with _update_infos_lock:
        _all_infos.add(info)
        if info._is_stepping():
            _infos_stepping.add(info)

# fmt: off
# IFDEF CYTHON
# cpdef remove_additional_info(PyDBAdditionalThreadInfo info):
# ELSE
def remove_additional_info(info):
# ENDIF
# fmt: on
    with _update_infos_lock:
        _all_infos.discard(info)
        _infos_stepping.discard(info)


# fmt: off
# IFDEF CYTHON
# cpdef bint any_thread_stepping():
# ELSE
def any_thread_stepping():
# ENDIF
# fmt: on
    return bool(_infos_stepping)
