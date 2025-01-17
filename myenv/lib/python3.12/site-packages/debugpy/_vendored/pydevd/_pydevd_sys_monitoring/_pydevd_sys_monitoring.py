# Copyright: Brainwy Software
#
# License: EPL

from collections import namedtuple
import dis
import os
import re
import sys
from _pydev_bundle._pydev_saved_modules import threading
from types import CodeType, FrameType
from typing import Dict, Optional, Tuple, Any
from os.path import basename, splitext

from _pydev_bundle import pydev_log
from _pydevd_bundle import pydevd_dont_trace
from _pydevd_bundle.pydevd_constants import (
    IS_PY313_OR_GREATER,
    GlobalDebuggerHolder,
    ForkSafeLock,
    PYDEVD_IPYTHON_CONTEXT,
    EXCEPTION_TYPE_USER_UNHANDLED,
    RETURN_VALUES_DICT,
    PYTHON_SUSPEND,
)
from pydevd_file_utils import (
    NORM_PATHS_AND_BASE_CONTAINER,
    get_abs_path_real_path_and_base_from_file,
    get_abs_path_real_path_and_base_from_frame,
)
from _pydevd_bundle.pydevd_trace_dispatch import should_stop_on_exception, handle_exception
from _pydevd_bundle.pydevd_constants import EXCEPTION_TYPE_HANDLED
from _pydevd_bundle.pydevd_trace_dispatch import is_unhandled_exception
from _pydevd_bundle.pydevd_breakpoints import stop_on_unhandled_exception
from _pydevd_bundle.pydevd_utils import get_clsname_for_code

# fmt: off
# IFDEF CYTHON
# import cython
# from _pydevd_bundle.pydevd_cython cimport set_additional_thread_info, any_thread_stepping, PyDBAdditionalThreadInfo
# ELSE
from _pydevd_bundle.pydevd_additional_thread_info import set_additional_thread_info, any_thread_stepping, PyDBAdditionalThreadInfo
# ENDIF
# fmt: on

try:
    from _pydevd_bundle.pydevd_bytecode_utils import get_smart_step_into_variant_from_frame_offset
except ImportError:

    def get_smart_step_into_variant_from_frame_offset(*args, **kwargs):
        return None


if hasattr(sys, "monitoring"):
    DEBUGGER_ID = sys.monitoring.DEBUGGER_ID
    monitor = sys.monitoring

_thread_local_info = threading.local()
_get_ident = threading.get_ident
_thread_active = threading._active  # noqa

CMD_STEP_INTO: int = 107
CMD_STEP_OVER: int = 108
CMD_STEP_INTO_MY_CODE: int = 144
CMD_STEP_INTO_COROUTINE: int = 206
CMD_SMART_STEP_INTO: int = 128
can_skip: bool = True
CMD_STEP_RETURN: int = 109
CMD_STEP_OVER_MY_CODE: int = 159
CMD_STEP_RETURN_MY_CODE: int = 160
CMD_SET_BREAK: int = 111
CMD_SET_FUNCTION_BREAK: int = 208
STATE_RUN: int = 1
STATE_SUSPEND: int = 2

IGNORE_EXCEPTION_TAG = re.compile("[^#]*#.*@IgnoreException")
DEBUG_START = ("pydevd.py", "run")
DEBUG_START_PY3K = ("_pydev_execfile.py", "execfile")
TRACE_PROPERTY = "pydevd_traceproperty.py"

_global_notify_skipped_step_in = False
_global_notify_skipped_step_in_lock = ForkSafeLock()


# fmt: off
# IFDEF CYTHON
# cdef _notify_skipped_step_in_because_of_filters(py_db, frame):
# ELSE
def _notify_skipped_step_in_because_of_filters(py_db, frame):
# ENDIF
# fmt: on
    global _global_notify_skipped_step_in

    with _global_notify_skipped_step_in_lock:
        if _global_notify_skipped_step_in:
            # Check with lock in place (callers should actually have checked
            # before without the lock in place due to performance).
            return
        _global_notify_skipped_step_in = True
        py_db.notify_skipped_step_in_because_of_filters(frame)


# Easy for cython: always get the one at level 0 as that's the caller frame
# (on Python we have to control the depth to get the first user frame).
# fmt: off
# IFDEF CYTHON
# @cython.cfunc
# def _getframe(depth=0):
#     return sys._getframe()
# ELSE
_getframe = sys._getframe
# ENDIF
# fmt: on


# fmt: off
# IFDEF CYTHON
# cdef _get_bootstrap_frame(depth):
# ELSE
def _get_bootstrap_frame(depth: int) -> Tuple[Optional[FrameType], bool]:
# ENDIF
# fmt: on
    try:
        return _thread_local_info.f_bootstrap, _thread_local_info.is_bootstrap_frame_internal
    except:
        frame = _getframe(depth)
        f_bootstrap = frame
        # print('called at', f_bootstrap.f_code.co_name, f_bootstrap.f_code.co_filename, f_bootstrap.f_code.co_firstlineno)
        is_bootstrap_frame_internal = False
        while f_bootstrap is not None:
            filename = f_bootstrap.f_code.co_filename
            name = splitext(basename(filename))[0]

            if name == "threading":
                if f_bootstrap.f_code.co_name in ("__bootstrap", "_bootstrap"):
                    # We need __bootstrap_inner, not __bootstrap.
                    return None, False

                elif f_bootstrap.f_code.co_name in ("__bootstrap_inner", "_bootstrap_inner", "is_alive"):
                    # Note: be careful not to use threading.current_thread to avoid creating a dummy thread.
                    is_bootstrap_frame_internal = True
                    break

            elif name == "pydev_monkey":
                if f_bootstrap.f_code.co_name == "__call__":
                    is_bootstrap_frame_internal = True
                    break

            elif name == "pydevd":
                if f_bootstrap.f_code.co_name in ("run", "main"):
                    # We need to get to _exec
                    return None, False

                if f_bootstrap.f_code.co_name == "_exec":
                    is_bootstrap_frame_internal = True
                    break

            elif f_bootstrap.f_back is None:
                break

            f_bootstrap = f_bootstrap.f_back

        if f_bootstrap is not None:
            _thread_local_info.is_bootstrap_frame_internal = is_bootstrap_frame_internal
            _thread_local_info.f_bootstrap = f_bootstrap
            return _thread_local_info.f_bootstrap, _thread_local_info.is_bootstrap_frame_internal

        return f_bootstrap, is_bootstrap_frame_internal


# fmt: off
# IFDEF CYTHON
# cdef _get_unhandled_exception_frame(exc, int depth):
# ELSE
def _get_unhandled_exception_frame(exc, depth: int) -> Optional[FrameType]:
# ENDIF
# fmt: on
    try:
        # Unhandled frame has to be from the same exception.
        if _thread_local_info.f_unhandled_exc is exc:
            return _thread_local_info.f_unhandled_frame
        else:
            del _thread_local_info.f_unhandled_frame
            del _thread_local_info.f_unhandled_exc
            raise AttributeError('Not the same exception')
    except:
        f_unhandled = _getframe(depth)

        while f_unhandled is not None and f_unhandled.f_back is not None:
            f_back = f_unhandled.f_back
            filename = f_back.f_code.co_filename
            name = splitext(basename(filename))[0]

            # When the back frame is the bootstrap (or if we have no back
            # frame) then use this frame as the one to track.
            if name == "threading":
                if f_back.f_code.co_name in ("__bootstrap", "_bootstrap", "__bootstrap_inner", "_bootstrap_inner", "run"):
                    break

            elif name == "pydev_monkey":
                if f_back.f_code.co_name == "__call__":
                    break

            elif name == "pydevd":
                if f_back.f_code.co_name in ("_exec", "run", "main"):
                    break

            elif name == "pydevd_runpy":
                if f_back.f_code.co_name.startswith(("run", "_run")):
                    break

            elif name == "<frozen runpy>":
                if f_back.f_code.co_name.startswith(("run", "_run")):
                    break

            elif name == "runpy":
                if f_back.f_code.co_name.startswith(("run", "_run")):
                    break

            f_unhandled = f_back

        if f_unhandled is not None:
            _thread_local_info.f_unhandled_frame = f_unhandled
            _thread_local_info.f_unhandled_exc = exc
            return _thread_local_info.f_unhandled_frame

        return f_unhandled


# fmt: off
# IFDEF CYTHON
# cdef class ThreadInfo:
#     cdef unsigned long thread_ident
#     cdef PyDBAdditionalThreadInfo additional_info
#     thread: threading.Thread
#     trace: bool
#     _use_is_stopped: bool
# ELSE
class ThreadInfo:
    additional_info: PyDBAdditionalThreadInfo
    thread_ident: int
    thread: threading.Thread
    trace: bool
# ENDIF
# fmt: on

    # fmt: off
    # IFDEF CYTHON
    # def __init__(self, thread, unsigned long thread_ident, bint trace, PyDBAdditionalThreadInfo additional_info):
    # ELSE
    def __init__(self, thread: threading.Thread, thread_ident: int, trace: bool, additional_info: PyDBAdditionalThreadInfo):
    # ENDIF
    # fmt: on
        self.thread = thread
        self.thread_ident = thread_ident
        self.additional_info = additional_info
        self.trace = trace
        self._use_is_stopped = hasattr(thread, '_is_stopped')
        
    # fmt: off
    # IFDEF CYTHON
    # cdef bint is_thread_alive(self):
    # ELSE
    def is_thread_alive(self):
    # ENDIF
    # fmt: on
        if self._use_is_stopped:
            return not self.thread._is_stopped
        else:
            return not self.thread._handle.is_done()


class _DeleteDummyThreadOnDel:
    """
    Helper class to remove a dummy thread from threading._active on __del__.
    """

    def __init__(self, dummy_thread):
        self._dummy_thread = dummy_thread
        self._tident = dummy_thread.ident
        # Put the thread on a thread local variable so that when
        # the related thread finishes this instance is collected.
        #
        # Note: no other references to this instance may be created.
        # If any client code creates a reference to this instance,
        # the related _DummyThread will be kept forever!
        _thread_local_info._track_dummy_thread_ref = self

    def __del__(self):
        with threading._active_limbo_lock:
            if _thread_active.get(self._tident) is self._dummy_thread:
                _thread_active.pop(self._tident, None)


# fmt: off
# IFDEF CYTHON
# cdef _create_thread_info(depth):
#     cdef unsigned long thread_ident
# ELSE
def _create_thread_info(depth):
# ENDIF
# fmt: on
    # Don't call threading.currentThread because if we're too early in the process
    # we may create a dummy thread.
    thread_ident = _get_ident()

    f_bootstrap_frame, is_bootstrap_frame_internal = _get_bootstrap_frame(depth + 1)
    if f_bootstrap_frame is None:
        return None  # Case for threading when it's still in bootstrap or early in pydevd.

    if is_bootstrap_frame_internal:
        t = None
        if f_bootstrap_frame.f_code.co_name in ("__bootstrap_inner", "_bootstrap_inner", "is_alive"):
            # Note: be careful not to use threading.current_thread to avoid creating a dummy thread.
            t = f_bootstrap_frame.f_locals.get("self")
            if not isinstance(t, threading.Thread):
                t = None

        elif f_bootstrap_frame.f_code.co_name in ("_exec", "__call__"):
            # Note: be careful not to use threading.current_thread to avoid creating a dummy thread.
            t = f_bootstrap_frame.f_locals.get("t")
            if not isinstance(t, threading.Thread):
                t = None

    else:
        # This means that the first frame is not in threading nor in pydevd.
        # In practice this means it's some unmanaged thread, so, creating
        # a dummy thread is ok in this use-case.
        t = threading.current_thread()

    if t is None:
        t = _thread_active.get(thread_ident)

    if isinstance(t, threading._DummyThread) and not IS_PY313_OR_GREATER:
        _thread_local_info._ref = _DeleteDummyThreadOnDel(t)

    if t is None:
        return None

    if getattr(t, "is_pydev_daemon_thread", False):
        return ThreadInfo(t, thread_ident, False, None)
    else:
        try:
            additional_info = t.additional_info
            if additional_info is None:
                raise AttributeError()
        except:
            additional_info = set_additional_thread_info(t)
        return ThreadInfo(t, thread_ident, True, additional_info)


# fmt: off
# IFDEF CYTHON
# cdef class FuncCodeInfo:
#     cdef str co_filename
#     cdef str canonical_normalized_filename
#     cdef str abs_path_filename
#     cdef bint always_skip_code
#     cdef bint breakpoint_found
#     cdef bint function_breakpoint_found
#     cdef bint plugin_line_breakpoint_found
#     cdef bint plugin_call_breakpoint_found
#     cdef bint plugin_line_stepping
#     cdef bint plugin_call_stepping
#     cdef bint plugin_return_stepping
#     cdef int pydb_mtime
#     cdef dict bp_line_to_breakpoint
#     cdef object function_breakpoint
#     cdef bint always_filtered_out
#     cdef bint filtered_out_force_checked
#     cdef object try_except_container_obj
#     cdef object code_obj
#     cdef str co_name
# ELSE
class FuncCodeInfo:

# ENDIF
# fmt: on
    def __init__(self):
        self.co_filename: str = ""
        self.canonical_normalized_filename: str = ""
        self.abs_path_filename: str = ""

        # These is never seen and we never stop, even if it's a callback coming
        # from user code (these are completely invisible to the debugging tracing).
        self.always_skip_code: bool = False

        self.breakpoint_found: bool = False
        self.function_breakpoint_found: bool = False

        # A plugin can choose whether to stop on function calls or line events.
        self.plugin_line_breakpoint_found: bool = False
        self.plugin_call_breakpoint_found: bool = False

        self.plugin_line_stepping: bool = False
        self.plugin_call_stepping: bool = False
        self.plugin_return_stepping: bool = False

        # When pydb_mtime != PyDb.mtime the validity of breakpoints have
        # to be re-evaluated (if invalid a new FuncCodeInfo must be created and
        # tracing can't be disabled for the related frames).
        self.pydb_mtime: int = -1

        self.bp_line_to_breakpoint: Dict[int, Any] = {}
        self.function_breakpoint = None

        # This means some file is globally filtered out during debugging. Note
        # that we may still need to pause in it (in a step return to user code,
        # we may need to track this one).
        self.always_filtered_out: bool = False

        # This should be used to filter code in a CMD_STEP_INTO_MY_CODE
        # (and other XXX_MY_CODE variants).
        self.filtered_out_force_checked: bool = False

        self.try_except_container_obj: Optional[_TryExceptContainerObj] = None
        self.code_obj: CodeType = None
        self.co_name: str = ""

    def get_line_of_offset(self, offset):
        for start, end, line in self.code_obj.co_lines():
            if start is not None and end is not None and line is not None:
                if offset >= start and offset <= end:
                    return line
        return -1


# fmt: off
# IFDEF CYTHON
# cdef _get_thread_info(bint create, int depth):
# ELSE
def _get_thread_info(create: bool, depth: int) -> Optional[ThreadInfo]:
# ENDIF
# fmt: on
    """
    Provides thread-related info.

    May return None if the thread is still not active.
    """
    try:
        # Note: changing to a `dict[thread.ident] = thread_info` had almost no
        # effect in the performance.
        return _thread_local_info.thread_info
    except:
        if not create:
            return None
        thread_info = _create_thread_info(depth + 1)
        if thread_info is None:
            return None

        _thread_local_info.thread_info = thread_info
        return _thread_local_info.thread_info


# fmt: off
# IFDEF CYTHON
# cdef class _CodeLineInfo:
#     cdef dict line_to_offset
#     cdef int first_line
#     cdef int last_line
# ELSE
class _CodeLineInfo:
    line_to_offset: Dict[int, Any]
    first_line: int
    last_line: int
# ENDIF
# fmt: on

    # fmt: off
    # IFDEF CYTHON
    # def __init__(self, dict line_to_offset, int first_line, int last_line):
    #     self.line_to_offset = line_to_offset
    #     self.first_line = first_line
    #     self.last_line = last_line
    # ELSE
    def __init__(self, line_to_offset, first_line, last_line):
        self.line_to_offset = line_to_offset
        self.first_line = first_line
        self.last_line = last_line

    # ENDIF
    # fmt: on

# Note: this method has a version in cython too
# fmt: off
# IFDEF CYTHON
# cdef _CodeLineInfo _get_code_line_info(code_obj, _cache={}):
# ELSE
def _get_code_line_info(code_obj, _cache={}) -> _CodeLineInfo:
# ENDIF
# fmt: on
    try:
        return _cache[code_obj]
    except:
        line_to_offset = {}
        first_line = None
        last_line = None

        for offset, line in dis.findlinestarts(code_obj):
            if line is not None:
                line_to_offset[line] = offset

        if len(line_to_offset):
            first_line = min(line_to_offset)
            last_line = max(line_to_offset)
        ret = _CodeLineInfo(line_to_offset, first_line, last_line)
        _cache[code_obj] = ret
        return ret


_code_to_func_code_info_cache: Dict[CodeType, "FuncCodeInfo"] = {}


# fmt: off
# IFDEF CYTHON
# cpdef FuncCodeInfo _get_func_code_info(code_obj, frame_or_depth):
#     cdef FuncCodeInfo func_code_info
# ELSE
def _get_func_code_info(code_obj, frame_or_depth) -> FuncCodeInfo:
# ENDIF
# fmt: on
    """
    Provides code-object related info.

    Note that it contains informations on the breakpoints for a given function.
    If breakpoints change a new FuncCodeInfo instance will be created.

    Note that this can be called by any thread.
    """
    py_db = GlobalDebuggerHolder.global_dbg
    if py_db is None:
        return None

    func_code_info = _code_to_func_code_info_cache.get(code_obj)
    if func_code_info is not None:
        if func_code_info.pydb_mtime == py_db.mtime:
            # if DEBUG:
            # print('_get_func_code_info: matched mtime', key, code_obj)
            return func_code_info

    # fmt: off
    # IFDEF CYTHON
    # cdef dict cache_file_type
    # cdef tuple cache_file_type_key
    # cdef PyCodeObject * code
    # cdef str co_filename
    # cdef str co_name
    # code = <PyCodeObject *> code_obj
    # co_filename = <str> code.co_filename
    # co_name = <str> code.co_name
    # ELSE
    cache_file_type: dict
    cache_file_type_key: tuple
    code = code_obj
    co_filename: str = code.co_filename
    co_name: str = code.co_name
    # ENDIF
    # fmt: on

    # print('_get_func_code_info: new (mtime did not match)', key, code_obj)

    func_code_info = FuncCodeInfo()
    func_code_info.code_obj = code_obj
    code_line_info = _get_code_line_info(code_obj)
    line_to_offset = code_line_info.line_to_offset
    func_code_info.pydb_mtime = py_db.mtime

    func_code_info.co_filename = co_filename
    func_code_info.co_name = co_name

    # Compute whether to always skip this.
    try:
        abs_path_real_path_and_base = NORM_PATHS_AND_BASE_CONTAINER[co_filename]
    except:
        abs_path_real_path_and_base = get_abs_path_real_path_and_base_from_file(co_filename)

    func_code_info.abs_path_filename = abs_path_real_path_and_base[0]
    func_code_info.canonical_normalized_filename = abs_path_real_path_and_base[1]

    frame = None
    cache_file_type = py_db.get_cache_file_type()
    # Note: this cache key must be the same from PyDB.get_file_type() -- see it for comments
    # on the cache.
    cache_file_type_key = (code.co_firstlineno, abs_path_real_path_and_base[0], code_obj)
    try:
        file_type = cache_file_type[cache_file_type_key]  # Make it faster
    except:
        if frame is None:
            if frame_or_depth.__class__ == int:
                frame = _getframe(frame_or_depth + 1)
            else:
                frame = frame_or_depth
            assert frame.f_code is code_obj, "%s != %s" % (frame.f_code, code_obj)

        file_type = py_db.get_file_type(frame, abs_path_real_path_and_base)  # we don't want to debug anything related to pydevd

    if file_type is not None:
        func_code_info.always_skip_code = True
        func_code_info.always_filtered_out = True
        _code_to_func_code_info_cache[code_obj] = func_code_info
        return func_code_info

    # still not set, check for dont trace comments.
    if pydevd_dont_trace.should_trace_hook is not None:
        # I.e.: cache the result skip (no need to evaluate the same frame multiple times).
        # Note that on a code reload, we won't re-evaluate this because in practice, the frame.f_code
        # Which will be handled by this frame is read-only, so, we can cache it safely.
        if not pydevd_dont_trace.should_trace_hook(code_obj, func_code_info.abs_path_filename):
            if frame is None:
                if frame_or_depth.__class__ == int:
                    frame = _getframe(frame_or_depth + 1)
                else:
                    frame = frame_or_depth
            assert frame.f_code is code_obj

            func_code_info.always_filtered_out = True
            _code_to_func_code_info_cache[code_obj] = func_code_info
            return func_code_info

    if frame is None:
        if frame_or_depth.__class__ == int:
            frame = _getframe(frame_or_depth + 1)
        else:
            frame = frame_or_depth
        assert frame.f_code is code_obj

    func_code_info.filtered_out_force_checked = py_db.apply_files_filter(frame, func_code_info.abs_path_filename, True)

    if py_db.is_files_filter_enabled:
        func_code_info.always_filtered_out = func_code_info.filtered_out_force_checked
        if func_code_info.always_filtered_out:
            _code_to_func_code_info_cache[code_obj] = func_code_info
            return func_code_info

    else:
        func_code_info.always_filtered_out = False

    # Handle regular breakpoints
    breakpoints: dict = py_db.breakpoints.get(func_code_info.canonical_normalized_filename)
    function_breakpoint: object = py_db.function_breakpoint_name_to_breakpoint.get(func_code_info.co_name)
    # print('\n---')
    # print(py_db.breakpoints)
    # print(func_code_info.canonical_normalized_filename)
    # print(py_db.breakpoints.get(func_code_info.canonical_normalized_filename))
    if function_breakpoint:
        # Go directly into tracing mode
        func_code_info.function_breakpoint_found = True
        func_code_info.function_breakpoint = function_breakpoint

    if breakpoints:
        # if DEBUG:
        #    print('found breakpoints', code_obj_py.co_name, breakpoints)

        bp_line_to_breakpoint = {}

        for breakpoint_line, bp in breakpoints.items():
            if breakpoint_line in line_to_offset:
                bp_line_to_breakpoint[breakpoint_line] = bp

        func_code_info.breakpoint_found = bool(bp_line_to_breakpoint)
        func_code_info.bp_line_to_breakpoint = bp_line_to_breakpoint

    if py_db.plugin:
        plugin_manager = py_db.plugin
        is_tracked_frame = plugin_manager.is_tracked_frame(frame)

        if is_tracked_frame:
            if py_db.has_plugin_line_breaks:
                required_events_breakpoint = plugin_manager.required_events_breakpoint()
                func_code_info.plugin_line_breakpoint_found = "line" in required_events_breakpoint
                func_code_info.plugin_call_breakpoint_found = "call" in required_events_breakpoint

            required_events_stepping = plugin_manager.required_events_stepping()
            func_code_info.plugin_line_stepping: bool = "line" in required_events_stepping
            func_code_info.plugin_call_stepping: bool = "call" in required_events_stepping
            func_code_info.plugin_return_stepping: bool = "return" in required_events_stepping

    _code_to_func_code_info_cache[code_obj] = func_code_info
    return func_code_info


# fmt: off
# IFDEF CYTHON
# cdef _enable_line_tracing(code):
# ELSE
def _enable_line_tracing(code):
# ENDIF
# fmt: on
    # print('enable line tracing', code)
    _ensure_monitoring()
    events = monitor.get_local_events(DEBUGGER_ID, code)
    monitor.set_local_events(DEBUGGER_ID, code, events | monitor.events.LINE | monitor.events.JUMP)


# fmt: off
# IFDEF CYTHON
# cdef _enable_return_tracing(code):
# ELSE
def _enable_return_tracing(code):
# ENDIF
# fmt: on
    # print('enable return tracing', code)
    _ensure_monitoring()
    events = monitor.get_local_events(DEBUGGER_ID, code)
    monitor.set_local_events(DEBUGGER_ID, code, events | monitor.events.PY_RETURN)


# fmt: off
# IFDEF CYTHON
# cpdef disable_code_tracing(code):
# ELSE
def disable_code_tracing(code):
# ENDIF
# fmt: on
    _ensure_monitoring()
    monitor.set_local_events(DEBUGGER_ID, code, 0)


# fmt: off
# IFDEF CYTHON
# cpdef enable_code_tracing(unsigned long thread_ident, code, frame):
# ELSE
def enable_code_tracing(thread_ident: Optional[int], code, frame) -> bool:
# ENDIF
# fmt: on
    """
    Note: this must enable code tracing for the given code/frame.

    The frame can be from any thread!

    :return: Whether code tracing was added in this function to the given code.
    """
    # DEBUG = False  # 'my_code.py' in code.co_filename or 'other.py' in code.co_filename
    # if DEBUG:
    #     print('==== enable code tracing', code.co_filename[-30:], code.co_name)
    py_db: object = GlobalDebuggerHolder.global_dbg
    if py_db is None or py_db.pydb_disposed:
        return False

    func_code_info: FuncCodeInfo = _get_func_code_info(code, frame)
    if func_code_info.always_skip_code:
        # if DEBUG:
        #     print('disable (always skip)')
        return False

    try:
        thread = threading._active.get(thread_ident)
        if thread is None:
            return False
        additional_info = set_additional_thread_info(thread)
    except:
        # Cannot set based on stepping
        return False

    return _enable_code_tracing(py_db, additional_info, func_code_info, code, frame, False)


# fmt: off
# IFDEF CYTHON
# cdef bint _enable_code_tracing(py_db, PyDBAdditionalThreadInfo additional_info, FuncCodeInfo func_code_info, code, frame, bint warn_on_filtered_out):
#     cdef int step_cmd
#     cdef bint is_stepping
#     cdef bint code_tracing_added
# ELSE
def _enable_code_tracing(py_db, additional_info, func_code_info: FuncCodeInfo, code, frame, warn_on_filtered_out) -> bool:
# ENDIF
# fmt: on
    """
    :return: Whether code tracing was added in this function to the given code.
    """
    # DEBUG = False  # 'my_code.py' in code.co_filename or 'other.py' in code.co_filename
    step_cmd = additional_info.pydev_step_cmd
    is_stepping = step_cmd != -1
    code_tracing_added = False

    if func_code_info.always_filtered_out:
        # if DEBUG:
        #     print('disable (always filtered out)')
        if (
            warn_on_filtered_out
            and is_stepping
            and additional_info.pydev_original_step_cmd in (CMD_STEP_INTO, CMD_STEP_INTO_MY_CODE)
            and not _global_notify_skipped_step_in
        ):
            _notify_skipped_step_in_because_of_filters(py_db, frame)

        if is_stepping:
            # Tracing may be needed for return value
            _enable_step_tracing(py_db, code, step_cmd, additional_info, frame)
            code_tracing_added = True
        return code_tracing_added

    if func_code_info.breakpoint_found or func_code_info.plugin_line_breakpoint_found:
        _enable_line_tracing(code)
        code_tracing_added = True

    if is_stepping:
        _enable_step_tracing(py_db, code, step_cmd, additional_info, frame)
        code_tracing_added = True

    return code_tracing_added


# fmt: off
# IFDEF CYTHON
# cdef _enable_step_tracing(py_db, code, step_cmd, PyDBAdditionalThreadInfo info, frame):
# ELSE
def _enable_step_tracing(py_db, code, step_cmd, info, frame):
# ENDIF
# fmt: on
    if step_cmd in (CMD_STEP_INTO, CMD_STEP_INTO_MY_CODE, CMD_STEP_INTO_COROUTINE, CMD_SMART_STEP_INTO):
        # Stepping (must have line/return tracing enabled).
        _enable_line_tracing(code)
        _enable_return_tracing(code)

    elif step_cmd in (CMD_STEP_RETURN, CMD_STEP_RETURN_MY_CODE) and _is_same_frame(info, info.pydev_step_stop, frame):
        _enable_return_tracing(code)

    elif step_cmd in (CMD_STEP_OVER, CMD_STEP_OVER_MY_CODE):
        if _is_same_frame(info, info.pydev_step_stop, frame):
            _enable_line_tracing(code)

            # Wee need to enable return tracing because if we have a return during a step over
            # we need to stop too.
            _enable_return_tracing(code)
        elif py_db.show_return_values and _is_same_frame(info, info.pydev_step_stop, frame.f_back):
            # Show return values on step over.
            _enable_return_tracing(code)


# fmt: off
# IFDEF CYTHON
# cdef class _TryExceptContainerObj:
#     cdef list try_except_infos
# ELSE
class _TryExceptContainerObj:
# ENDIF
# fmt: on
    """
    A dumb container object just to contain the try..except info when needed. Meant to be
    persistent among multiple PyDBFrames to the same code object.
    """

    # fmt: off
    # IFDEF CYTHON
    # def __init__(self, list try_except_infos):
    #     self.try_except_infos = try_except_infos
    # ELSE
    def __init__(self, try_except_infos):
        self.try_except_infos = try_except_infos

    # ENDIF
    # fmt: on


# fmt: off
# IFDEF CYTHON
# cdef _unwind_event(code, instruction, exc):
#     cdef ThreadInfo thread_info
#     cdef FuncCodeInfo func_code_info
# ELSE
def _unwind_event(code, instruction, exc):
# ENDIF
# fmt: on
    try:
        thread_info = _thread_local_info.thread_info
    except:
        thread_info = _get_thread_info(True, 1)
        if thread_info is None:
            return

    py_db: object = GlobalDebuggerHolder.global_dbg
    if py_db is None or py_db.pydb_disposed:
        return

    if not thread_info.trace or not thread_info.is_thread_alive():
        # For thread-related stuff we can't disable the code tracing because other
        # threads may still want it...
        return

    func_code_info: FuncCodeInfo = _get_func_code_info(code, 1)
    if func_code_info.always_skip_code:
        return

    # print('_unwind_event', code, exc)
    frame = _getframe(1)
    arg = (type(exc), exc, exc.__traceback__)

    has_caught_exception_breakpoint_in_pydb = (
        py_db.break_on_caught_exceptions or py_db.break_on_user_uncaught_exceptions or py_db.has_plugin_exception_breaks
    )

    if has_caught_exception_breakpoint_in_pydb:
        _should_stop, frame, user_uncaught_exc_info = should_stop_on_exception(
            py_db, thread_info.additional_info, frame, thread_info.thread, arg, None, is_unwind=True
        )
        if user_uncaught_exc_info:
            # TODO: Check: this may no longer be needed as in the unwind we know it's
            # an exception bubbling up (wait for all tests to pass to check it).
            if func_code_info.try_except_container_obj is None:
                container_obj = _TryExceptContainerObj(py_db.collect_try_except_info(frame.f_code))
                func_code_info.try_except_container_obj = container_obj

            is_unhandled = is_unhandled_exception(
                func_code_info.try_except_container_obj, py_db, frame, user_uncaught_exc_info[1], user_uncaught_exc_info[2]
            )

            if is_unhandled:
                handle_exception(py_db, thread_info.thread, frame, user_uncaught_exc_info[0], EXCEPTION_TYPE_USER_UNHANDLED)
                return

    break_on_uncaught_exceptions = py_db.break_on_uncaught_exceptions
    if break_on_uncaught_exceptions:
        if frame is _get_unhandled_exception_frame(exc, 1):
            stop_on_unhandled_exception(py_db, thread_info.thread, thread_info.additional_info, arg)
            return


# fmt: off
# IFDEF CYTHON
# cdef _raise_event(code, instruction, exc):
#     cdef ThreadInfo thread_info
#     cdef FuncCodeInfo func_code_info
# ELSE
def _raise_event(code, instruction, exc):
# ENDIF
# fmt: on
    """
    The way this should work is the following: when the user is using
    pydevd to do the launch and we're on a managed stack, we should consider
    unhandled only if it gets into a pydevd. If it's a thread, if it stops
    inside the threading and if it's an unmanaged thread (i.e.: QThread)
    then stop if it doesn't have a back frame.

    Note: unlike other events, this one is global and not per-code (so,
    it cannot be individually enabled/disabled for a given code object).
    """
    try:
        thread_info = _thread_local_info.thread_info
    except:
        thread_info = _get_thread_info(True, 1)
        if thread_info is None:
            return
        
    py_db: object = GlobalDebuggerHolder.global_dbg
    if py_db is None or py_db.pydb_disposed:
        return

    if not thread_info.trace or not thread_info.is_thread_alive():
        # For thread-related stuff we can't disable the code tracing because other
        # threads may still want it...
        return

    func_code_info: FuncCodeInfo = _get_func_code_info(code, 1)
    if func_code_info.always_skip_code:
        return

    frame = _getframe(1)
    arg = (type(exc), exc, exc.__traceback__)

    # Compute the previous exception info (if any). We use it to check if the exception
    # should be stopped
    prev_exc_info = _thread_local_info._user_uncaught_exc_info if hasattr(_thread_local_info, "_user_uncaught_exc_info") else None
    should_stop, frame, _user_uncaught_exc_info = should_stop_on_exception(
        py_db, thread_info.additional_info, frame, thread_info.thread, arg, prev_exc_info
    )

    # Save the current exception info for the next raise event.
    _thread_local_info._user_uncaught_exc_info = _user_uncaught_exc_info

    # print('!!!! should_stop (in raise)', should_stop)
    if should_stop:
        handle_exception(py_db, thread_info.thread, frame, arg, EXCEPTION_TYPE_HANDLED)


# fmt: off
# IFDEF CYTHON
# cdef str get_func_name(frame):
#     cdef str func_name
# ELSE
def get_func_name(frame):
# ENDIF
# fmt: on
    code_obj = frame.f_code
    func_name = code_obj.co_name
    try:
        cls_name = get_clsname_for_code(code_obj, frame)
        if cls_name is not None:
            return "%s.%s" % (cls_name, func_name)
        else:
            return func_name
    except:
        pydev_log.exception()
        return func_name


# fmt: off
# IFDEF CYTHON
# cdef _show_return_values(frame, arg):
# ELSE
def _show_return_values(frame, arg):
# ENDIF
# fmt: on
    try:
        try:
            f_locals_back = getattr(frame.f_back, "f_locals", None)
            if f_locals_back is not None:
                return_values_dict = f_locals_back.get(RETURN_VALUES_DICT, None)
                if return_values_dict is None:
                    return_values_dict = {}
                    f_locals_back[RETURN_VALUES_DICT] = return_values_dict
                name = get_func_name(frame)
                return_values_dict[name] = arg
        except:
            pydev_log.exception()
    finally:
        f_locals_back = None


# fmt: off
# IFDEF CYTHON
# cdef _remove_return_values(py_db, frame):
# ELSE
def _remove_return_values(py_db, frame):
# ENDIF
# fmt: on
    try:
        try:
            # Showing return values was turned off, we should remove them from locals dict.
            # The values can be in the current frame or in the back one
            frame.f_locals.pop(RETURN_VALUES_DICT, None)

            f_locals_back = getattr(frame.f_back, "f_locals", None)
            if f_locals_back is not None:
                f_locals_back.pop(RETURN_VALUES_DICT, None)
        except:
            pydev_log.exception()
    finally:
        f_locals_back = None


# fmt: off
# IFDEF CYTHON
# cdef _return_event(code, instruction, retval):
#     cdef ThreadInfo thread_info
#     cdef FuncCodeInfo func_code_info
#     cdef PyDBAdditionalThreadInfo info
#     cdef int step_cmd
# ELSE
def _return_event(code, instruction, retval):
# ENDIF
# fmt: on
    try:
        thread_info = _thread_local_info.thread_info
    except:
        thread_info = _get_thread_info(True, 1)
        if thread_info is None:
            return

    py_db: object = GlobalDebuggerHolder.global_dbg
    if py_db is None or py_db.pydb_disposed:
        return monitor.DISABLE

    if not thread_info.trace or not thread_info.is_thread_alive():
        # For thread-related stuff we can't disable the code tracing because other
        # threads may still want it...
        return

    func_code_info: FuncCodeInfo = _get_func_code_info(code, 1)
    if func_code_info.always_skip_code:
        return monitor.DISABLE

    info = thread_info.additional_info

    # We know the frame depth.
    frame = _getframe(1)

    step_cmd = info.pydev_step_cmd
    if step_cmd == -1:
        return

    if info.suspend_type != PYTHON_SUSPEND:
        # Plugin stepping
        if func_code_info.plugin_return_stepping:
            _plugin_stepping(py_db, step_cmd, "return", frame, thread_info)
        return

    # Python line stepping
    stop_frame = info.pydev_step_stop
    if step_cmd in (CMD_STEP_INTO, CMD_STEP_INTO_MY_CODE, CMD_STEP_INTO_COROUTINE):
        force_check_project_scope = step_cmd == CMD_STEP_INTO_MY_CODE
        if frame.f_back is not None and not info.pydev_use_scoped_step_frame:
            back_func_code_info = _get_func_code_info(frame.f_back.f_code, frame.f_back)
            if (
                # Not filtered out.
                not back_func_code_info.always_skip_code
                and not back_func_code_info.always_filtered_out
                and not (force_check_project_scope and back_func_code_info.filtered_out_force_checked)
                # Prevent stopping in a return to the same location we were initially
                # (i.e.: double-stop at the same place due to some filtering).
                and info.step_in_initial_location != (frame.f_back, frame.f_back.f_lineno)
            ):
                if py_db.show_return_values:
                    _show_return_values(frame, retval)

                _stop_on_return(py_db, thread_info, info, step_cmd, frame, retval)
                return

    if step_cmd in (CMD_STEP_RETURN, CMD_STEP_RETURN_MY_CODE) and _is_same_frame(info, stop_frame, frame):
        if py_db.show_return_values:
            _show_return_values(frame, retval)

        _stop_on_return(py_db, thread_info, info, step_cmd, frame, retval)
        return

    elif (
        step_cmd in (CMD_STEP_OVER, CMD_STEP_OVER_MY_CODE)
        and not info.pydev_use_scoped_step_frame
        and _is_same_frame(info, stop_frame, frame)
    ):
        # This isn't in the sys.settrace version: on a step over, if we return and the return is valid, show
        # as a step return instead of going back to step into mode (but if the back frame is not valid, then
        # go to step into mode).
        f_back = frame.f_back
        if f_back is not None:
            back_func_code_info = _get_func_code_info(f_back.f_code, 2)
            force_check_project_scope = step_cmd == CMD_STEP_OVER_MY_CODE

            if (
                back_func_code_info is not None
                and not back_func_code_info.always_skip_code
                and not back_func_code_info.always_filtered_out
                and not (force_check_project_scope and back_func_code_info.filtered_out_force_checked)
            ):
                if py_db.show_return_values:
                    _show_return_values(frame, retval)

                _stop_on_return(py_db, thread_info, info, step_cmd, frame, retval)
                return

    elif step_cmd == CMD_SMART_STEP_INTO:
        if _is_same_frame(info, stop_frame, frame):
            # We're exiting the smart step into initial frame (so, we probably didn't find our target).
            if py_db.show_return_values:
                _show_return_values(frame, retval)

            _stop_on_return(py_db, thread_info, info, step_cmd, frame, retval)
            return

    if py_db.show_return_values:
        if (
            (
                info.pydev_step_cmd in (CMD_STEP_OVER, CMD_STEP_OVER_MY_CODE, CMD_SMART_STEP_INTO)
                and (_is_same_frame(info, stop_frame, frame.f_back))
            )
            or (info.pydev_step_cmd in (CMD_STEP_RETURN, CMD_STEP_RETURN_MY_CODE) and (info, _is_same_frame(info, stop_frame, frame)))
            or (info.pydev_step_cmd in (CMD_STEP_INTO, CMD_STEP_INTO_COROUTINE))
            or (
                info.pydev_step_cmd == CMD_STEP_INTO_MY_CODE
                and frame.f_back is not None
                and not py_db.apply_files_filter(frame.f_back, frame.f_back.f_code.co_filename, True)
            )
        ):
            _show_return_values(frame, retval)

    if step_cmd in (CMD_STEP_OVER, CMD_STEP_RETURN, CMD_STEP_OVER_MY_CODE, CMD_STEP_RETURN_MY_CODE, CMD_SMART_STEP_INTO):
        # If we are in single step mode and something causes us to exit the current frame, we need to make sure we break
        # eventually.  Force the step mode to step into and the step stop frame to None.
        # I.e.: F6 in the end of a function should stop in the next possible position (instead of forcing the user
        # to make a step in or step over at that location).
        # Note: this is especially troublesome when we're skipping code with the
        # @DontTrace comment.
        stop_frame = info.pydev_step_stop
        if stop_frame is frame and not info.pydev_use_scoped_step_frame:
            if step_cmd in (CMD_STEP_OVER, CMD_STEP_RETURN, CMD_SMART_STEP_INTO):
                info.pydev_step_cmd = CMD_STEP_INTO
            else:
                info.pydev_step_cmd = CMD_STEP_INTO_MY_CODE
            info.pydev_step_stop = None
            _enable_code_tracing_for_frame_and_parents(thread_info, stop_frame.f_back)
            if py_db.show_return_values:
                _show_return_values(frame, retval)


# fmt: off
# IFDEF CYTHON
# cdef _enable_code_tracing_for_frame_and_parents(ThreadInfo thread_info, frame):
#     cdef FuncCodeInfo func_code_info
# ELSE
def _enable_code_tracing_for_frame_and_parents(thread_info, frame):
# ENDIF
# fmt: on
    py_db: object = GlobalDebuggerHolder.global_dbg
    if py_db is None or py_db.pydb_disposed:
        return

    while frame is not None:
        func_code_info: FuncCodeInfo = _get_func_code_info(frame.f_code, frame)
        if func_code_info.always_skip_code:
            frame = frame.f_back
            continue

        _enable_code_tracing(py_db, thread_info.additional_info, func_code_info, frame.f_code, frame, False)
        frame = frame.f_back


# fmt: off
# IFDEF CYTHON
# cdef _stop_on_return(py_db, ThreadInfo thread_info, PyDBAdditionalThreadInfo info, int step_cmd, frame, retval):
# ELSE
def _stop_on_return(py_db, thread_info, info, step_cmd, frame, retval):
# ENDIF
# fmt: on
    back = frame.f_back
    if back is not None:
        # When we get to the pydevd run function, the debugging has actually finished for the main thread
        # (note that it can still go on for other threads, but for this one, we just make it finish)
        # So, just setting it to None should be OK
        back_absolute_filename, _, base = get_abs_path_real_path_and_base_from_frame(back)
        if (base, back.f_code.co_name) in (DEBUG_START, DEBUG_START_PY3K):
            back = None

        elif base == TRACE_PROPERTY:
            # We dont want to trace the return event of pydevd_traceproperty (custom property for debugging)
            # if we're in a return, we want it to appear to the user in the previous frame!
            return

        elif pydevd_dont_trace.should_trace_hook is not None:
            if not pydevd_dont_trace.should_trace_hook(back.f_code, back_absolute_filename):
                # In this case, we'll have to skip the previous one because it shouldn't be traced.
                # Also, we have to reset the tracing, because if the parent's parent (or some
                # other parent) has to be traced and it's not currently, we wouldn't stop where
                # we should anymore (so, a step in/over/return may not stop anywhere if no parent is traced).
                # Related test: _debugger_case17a.py
                py_db.set_trace_for_frame_and_parents(thread_info.thread_ident, back)
                return

    if back is not None:
        # if we're in a return, we want it to appear to the user in the previous frame!
        py_db.set_suspend(thread_info.thread, step_cmd, original_step_cmd=info.pydev_original_step_cmd)
        _do_wait_suspend(py_db, thread_info, back, "return", retval)
    else:
        # in jython we may not have a back frame
        info.pydev_step_stop = None
        info.pydev_original_step_cmd = -1
        info.pydev_step_cmd = -1
        info.pydev_state = STATE_RUN
        info.update_stepping_info()


# fmt: off
# IFDEF CYTHON
# cdef _stop_on_breakpoint(py_db, ThreadInfo thread_info, int stop_reason, bp, frame, new_frame, bint stop, bint stop_on_plugin_breakpoint, str bp_type):
#     cdef PyDBAdditionalThreadInfo additional_info
# ELSE
def _stop_on_breakpoint(
    py_db, thread_info: ThreadInfo, stop_reason: int, bp, frame, new_frame, stop: bool, stop_on_plugin_breakpoint: bool, bp_type: str
):
# ENDIF
# fmt: on
    """
    :param bp: the breakpoint hit (additional conditions will be checked now).
    :param frame: the actual frame
    :param new_frame: either the actual frame or the frame provided by the plugins.
    :param stop: whether we should do a regular line breakpoint.
    :param stop_on_plugin_breakpoint: whether we should stop in a plugin breakpoint.

    :return:
        True if the breakpoint was suspended inside this function and False otherwise.
        Note that even if False is returned, it's still possible
    """
    additional_info = thread_info.additional_info
    # ok, hit breakpoint, now, we have to discover if it is a conditional breakpoint
    # lets do the conditional stuff here
    if bp.expression is not None:
        # If it has an expression, it's always handled even if we don't stop.
        py_db.handle_breakpoint_expression(bp, additional_info, new_frame)

    if stop or stop_on_plugin_breakpoint:
        if bp.has_condition:
            eval_result = py_db.handle_breakpoint_condition(additional_info, bp, new_frame)
            if not eval_result:
                stop = False
                stop_on_plugin_breakpoint = False

    # Handle logpoint (on a logpoint we should never stop).
    if (stop or stop_on_plugin_breakpoint) and bp.is_logpoint:
        stop = False
        stop_on_plugin_breakpoint = False

        if additional_info.pydev_message is not None and len(additional_info.pydev_message) > 0:
            cmd = py_db.cmd_factory.make_io_message(additional_info.pydev_message + os.linesep, "1")
            py_db.writer.add_command(cmd)

    if stop:
        py_db.set_suspend(
            thread_info.thread,
            stop_reason,
            suspend_other_threads=bp and bp.suspend_policy == "ALL",
        )
        # print('suspend on breakpoint...')
        _do_wait_suspend(py_db, thread_info, frame, "line", None)
        return True

    elif stop_on_plugin_breakpoint:
        stop_at_frame = py_db.plugin.suspend(py_db, thread_info.thread, frame, bp_type)
        if stop_at_frame and thread_info.additional_info.pydev_state == STATE_SUSPEND:
            _do_wait_suspend(py_db, thread_info, stop_at_frame, "line", None)
        return

    return False


# fmt: off
# IFDEF CYTHON
# cdef _plugin_stepping(py_db, int step_cmd, event, frame, ThreadInfo thread_info):
#     cdef bint stop
#     cdef dict stop_info
# ELSE
def _plugin_stepping(py_db, step_cmd, event, frame, thread_info):
# ENDIF
# fmt: on
    plugin_manager = py_db.plugin
    # Step return makes no sense for plugins (I guess?!?), so, just handle as step into.
    if step_cmd in (CMD_STEP_INTO, CMD_STEP_INTO_MY_CODE, CMD_STEP_INTO_COROUTINE, CMD_SMART_STEP_INTO) or step_cmd in (
        CMD_STEP_RETURN,
        CMD_STEP_RETURN_MY_CODE,
    ):
        stop_info = {}
        stop = False
        result = plugin_manager.cmd_step_into(py_db, frame, event, thread_info.additional_info, thread_info.thread, stop_info, stop)
        if result:
            stop, plugin_stop = result
            if plugin_stop:
                plugin_manager.stop(py_db, frame, event, thread_info.thread, stop_info, None, step_cmd)
                return

    elif step_cmd in (CMD_STEP_OVER, CMD_STEP_OVER_MY_CODE):
        if plugin_manager is not None:
            stop_info = {}
            stop = False
            result = plugin_manager.cmd_step_over(py_db, frame, event, thread_info.additional_info, thread_info.thread, stop_info, stop)
            if result:
                stop, plugin_stop = result
                if plugin_stop:
                    plugin_manager.stop(py_db, frame, event, thread_info.thread, stop_info, None, step_cmd)
                    return


# fmt: off
# IFDEF CYTHON
# cdef _jump_event(code, int from_offset, int to_offset):
#     cdef ThreadInfo thread_info
#     cdef FuncCodeInfo func_code_info
#     cdef int from_line
#     cdef int to_line
# ELSE
def _jump_event(code, from_offset, to_offset):
# ENDIF
# fmt: on
    # A bunch of things have to be repeated especially because in the sys.monitoring
    # everything is global, yet, when we start tracing something for stepping that
    # needs to be per-thread.
    try:
        thread_info = _thread_local_info.thread_info
    except:
        thread_info = _get_thread_info(True, 1)
        if thread_info is None:
            return

    py_db: object = GlobalDebuggerHolder.global_dbg
    if py_db is None or py_db.pydb_disposed:
        return monitor.DISABLE

    # If we get another jump event, remove the extra check for the line event
    if hasattr(_thread_local_info, "f_disable_next_line_if_match"):
        del _thread_local_info.f_disable_next_line_if_match

    if not thread_info.trace or not thread_info.is_thread_alive():
        # For thread-related stuff we can't disable the code tracing because other
        # threads may still want it...
        return

    func_code_info: FuncCodeInfo = _get_func_code_info(code, 1)
    if func_code_info.always_skip_code or func_code_info.always_filtered_out:
        return monitor.DISABLE

    # Same logic as "sys_trace_jump_func" in https://github.com/python/cpython/blob/main/Python/legacy_tracing.c

    # Ignore forward jump.
    # print('jump event', code.co_name, 'from offset', from_offset, 'to offset', to_offset)
    if to_offset > from_offset:
        return monitor.DISABLE

    from_line = func_code_info.get_line_of_offset(from_offset or 0)
    to_line = func_code_info.get_line_of_offset(to_offset or 0)

    if from_line != to_line:
        # I.e.: use case: "yield from [j for j in a if j % 2 == 0]"
        return monitor.DISABLE

    # We know the frame depth.
    frame = _getframe(1)

    # Disable the next line event as we're jumping to a line. The line event will be redundant.
    _thread_local_info.f_disable_next_line_if_match = (func_code_info.co_filename, frame.f_lineno)
    # pydev_log.debug('_jump_event', code.co_name, 'from line', from_line, 'to line', frame.f_lineno)

    return _internal_line_event(func_code_info, frame, frame.f_lineno)


# fmt: off
# IFDEF CYTHON
# cdef _line_event(code, int line):
#     cdef ThreadInfo thread_info
#     cdef FuncCodeInfo func_code_info
# ELSE
def _line_event(code, line):
# ENDIF
# fmt: on

    # A bunch of things have to be repeated especially because in the sys.monitoring
    # everything is global, yet, when we start tracing something for stepping that
    # needs to be per-thread.
    try:
        thread_info = _thread_local_info.thread_info
    except:
        thread_info = _get_thread_info(True, 1)
        if thread_info is None:
            return

    py_db: object = GlobalDebuggerHolder.global_dbg
    if py_db is None or py_db.pydb_disposed:
        return monitor.DISABLE

    # If we get another line event, remove the extra check for the line event
    if hasattr(_thread_local_info, "f_disable_next_line_if_match"):
        (co_filename, line_to_skip) = _thread_local_info.f_disable_next_line_if_match
        del _thread_local_info.f_disable_next_line_if_match
        if line_to_skip is line and co_filename == code.co_filename:
            # The last jump already jumped to this line and we haven't had any
            # line events or jumps since then. We don't want to consider this line twice
            # pydev_log.debug('_line_event skipped', line)
            return

    if not thread_info.trace or not thread_info.is_thread_alive():
        # For thread-related stuff we can't disable the code tracing because other
        # threads may still want it...
        return
    
    func_code_info: FuncCodeInfo = _get_func_code_info(code, 1)
    if func_code_info.always_skip_code or func_code_info.always_filtered_out:
        return monitor.DISABLE

    # pydev_log.debug('_line_event', code.co_name, line)

    # We know the frame depth.
    frame = _getframe(1)
    return _internal_line_event(func_code_info, frame, line)


# fmt: off
# IFDEF CYTHON
# cdef _internal_line_event(FuncCodeInfo func_code_info, frame, int line):
#     cdef ThreadInfo thread_info
#     cdef PyDBAdditionalThreadInfo info
#     cdef int step_cmd
#     cdef bint stop
#     cdef bint stop_on_plugin_breakpoint
#     cdef int stop_reason
#     cdef bint force_check_project_scope
# ELSE
def _internal_line_event(func_code_info, frame, line):
# ENDIF
# fmt: on
    py_db: object = GlobalDebuggerHolder.global_dbg
    thread_info = _thread_local_info.thread_info
    info = thread_info.additional_info

    step_cmd = info.pydev_step_cmd

    # print('line event', info, id(info), thread_info.thread.name)
    # print('line event', info.pydev_state, line, threading.current_thread(), code)
    # If we reached here, it was not filtered out.

    if func_code_info.breakpoint_found:
        bp = None
        stop = False
        stop_on_plugin_breakpoint = False

        stop_info = {}
        stop_reason = CMD_SET_BREAK
        bp_type = None

        bp = func_code_info.bp_line_to_breakpoint.get(line)
        if bp is not None:
            new_frame = frame
            stop = True

        if bp:
            if _stop_on_breakpoint(py_db, thread_info, stop_reason, bp, frame, new_frame, stop, stop_on_plugin_breakpoint, "python-line"):
                return

    if func_code_info.plugin_line_breakpoint_found:
        result = py_db.plugin.get_breakpoint(py_db, frame, "line", info)
        if result:
            stop_reason = CMD_SET_BREAK
            stop = False
            stop_on_plugin_breakpoint = True
            bp, new_frame, bp_type = result
            _stop_on_breakpoint(py_db, thread_info, stop_reason, bp, frame, new_frame, stop, stop_on_plugin_breakpoint, bp_type)
            return

    if info.pydev_state == STATE_SUSPEND:
        # Note: it's possible that it was suspended with a pause (and we'd stop here too).
        # print('suspend (pause)...')
        _do_wait_suspend(py_db, thread_info, frame, "line", None)
        return

    # Ok, did not suspend due to a breakpoint, let's see if we're stepping.
    stop_frame = info.pydev_step_stop
    if step_cmd == -1:
        if func_code_info.breakpoint_found or func_code_info.plugin_line_breakpoint_found or any_thread_stepping():
            return None

        return monitor.DISABLE

    if info.suspend_type != PYTHON_SUSPEND:
        # Plugin stepping
        if func_code_info.plugin_line_stepping:
            _plugin_stepping(py_db, step_cmd, "line", frame, thread_info)
        return

    # Python stepping now
    if step_cmd in (CMD_STEP_INTO, CMD_STEP_INTO_MY_CODE, CMD_STEP_INTO_COROUTINE):
        force_check_project_scope = step_cmd == CMD_STEP_INTO_MY_CODE
        if not info.pydev_use_scoped_step_frame:
            if func_code_info.always_filtered_out or (force_check_project_scope and func_code_info.filtered_out_force_checked):
                return

            py_db.set_suspend(thread_info.thread, step_cmd, original_step_cmd=info.pydev_original_step_cmd)
            _do_wait_suspend(py_db, thread_info, frame, "line", None)
            return
        else:
            # Make sure we check the filtering inside ipython calls too...
            if func_code_info.always_filtered_out or (force_check_project_scope and func_code_info.filtered_out_force_checked):
                return

            stop = False
            # We can only stop inside the ipython call.
            filename = frame.f_code.co_filename
            if filename.endswith(".pyc"):
                filename = filename[:-1]

            if not filename.endswith(PYDEVD_IPYTHON_CONTEXT[0]):
                f = frame.f_back
                while f is not None:
                    if f.f_code.co_name == PYDEVD_IPYTHON_CONTEXT[1]:
                        f2 = f.f_back
                        if f2 is not None and f2.f_code.co_name == PYDEVD_IPYTHON_CONTEXT[2]:
                            pydev_log.debug("Stop inside ipython call")
                            py_db.set_suspend(thread_info.thread, step_cmd, original_step_cmd=info.pydev_original_step_cmd)
                            thread_info.additional_info.trace_suspend_type = "sys_monitor"
                            _do_wait_suspend(py_db, thread_info, frame, "line", None)
                            break
                    f = f.f_back

                del f

        # In scoped mode if step in didn't work in this context it won't work
        # afterwards anyways.
        return

    elif step_cmd in (CMD_STEP_OVER, CMD_STEP_OVER_MY_CODE):
        # Note: when dealing with a step over my code it's the same as a step over (the
        # difference is that when we return from a frame in one we go to regular step
        # into and in the other we go to a step into my code).
        if _is_same_frame(info, stop_frame, frame):
            py_db.set_suspend(thread_info.thread, step_cmd, original_step_cmd=info.pydev_original_step_cmd)
            _do_wait_suspend(py_db, thread_info, frame, "line", None)
            return

    elif step_cmd == CMD_SMART_STEP_INTO:
        stop = False
        back = frame.f_back
        if _is_same_frame(info, stop_frame, back):
            if info.pydev_smart_child_offset != -1:
                # i.e.: in this case, we're not interested in the pause in the parent, rather
                # we're interested in the pause in the child (when the parent is at the proper place).
                stop = False

            else:
                pydev_smart_parent_offset = info.pydev_smart_parent_offset

                pydev_smart_step_into_variants = info.pydev_smart_step_into_variants
                if pydev_smart_parent_offset >= 0 and pydev_smart_step_into_variants:
                    # Preferred mode (when the smart step into variants are available
                    # and the offset is set).
                    stop = get_smart_step_into_variant_from_frame_offset(
                        back.f_lasti, pydev_smart_step_into_variants
                    ) is get_smart_step_into_variant_from_frame_offset(pydev_smart_parent_offset, pydev_smart_step_into_variants)

                else:
                    # Only the name/line is available, so, check that.
                    curr_func_name = frame.f_code.co_name

                    # global context is set with an empty name
                    if curr_func_name in ("?", "<module>") or curr_func_name is None:
                        curr_func_name = ""
                    if curr_func_name == info.pydev_func_name and stop_frame.f_lineno == info.pydev_next_line:
                        stop = True

            if not stop:
                # In smart step into, if we didn't hit it in this frame once, that'll
                # not be the case next time either, so, disable tracing for this frame.
                return

        elif back is not None and _is_same_frame(info, stop_frame, back.f_back):
            # Ok, we have to track 2 stops at this point, the parent and the child offset.
            # This happens when handling a step into which targets a function inside a list comprehension
            # or generator (in which case an intermediary frame is created due to an internal function call).
            pydev_smart_parent_offset = info.pydev_smart_parent_offset
            pydev_smart_child_offset = info.pydev_smart_child_offset
            # print('matched back frame', pydev_smart_parent_offset, pydev_smart_child_offset)
            # print('parent f_lasti', back.f_back.f_lasti)
            # print('child f_lasti', back.f_lasti)
            stop = False
            if pydev_smart_child_offset >= 0 and pydev_smart_child_offset >= 0:
                pydev_smart_step_into_variants = info.pydev_smart_step_into_variants

                if pydev_smart_parent_offset >= 0 and pydev_smart_step_into_variants:
                    # Note that we don't really check the parent offset, only the offset of
                    # the child (because this is a generator, the parent may have moved forward
                    # already -- and that's ok, so, we just check that the parent frame
                    # matches in this case).
                    smart_step_into_variant = get_smart_step_into_variant_from_frame_offset(
                        pydev_smart_parent_offset, pydev_smart_step_into_variants
                    )
                    # print('matched parent offset', pydev_smart_parent_offset)
                    # Ok, now, check the child variant
                    children_variants = smart_step_into_variant.children_variants
                    stop = children_variants and (
                        get_smart_step_into_variant_from_frame_offset(back.f_lasti, children_variants)
                        is get_smart_step_into_variant_from_frame_offset(pydev_smart_child_offset, children_variants)
                    )
                    # print('stop at child', stop)

            if not stop:
                # In smart step into, if we didn't hit it in this frame once, that'll
                # not be the case next time either, so, disable tracing for this frame.
                return

        if stop:
            py_db.set_suspend(thread_info.thread, step_cmd, original_step_cmd=info.pydev_original_step_cmd)
            _do_wait_suspend(py_db, thread_info, frame, "line", None)
            return


# fmt: off
# IFDEF CYTHON
# cdef _start_method_event(code, instruction_offset):
#     cdef ThreadInfo thread_info
#     cdef FuncCodeInfo func_code_info
#     cdef bint stop
#     cdef int stop_reason
#     cdef bint stop_on_plugin_breakpoint
#     cdef PyDBAdditionalThreadInfo info
#     cdef int step_cmd
#     cdef bint code_tracing_added
# ELSE
def _start_method_event(code, instruction_offset):
# ENDIF
# fmt: on
    try:
        thread_info = _thread_local_info.thread_info
    except:
        thread_info = _get_thread_info(True, 1)
        if thread_info is None:
            return

    py_db: object = GlobalDebuggerHolder.global_dbg
    if py_db is None or py_db.pydb_disposed:
        return monitor.DISABLE

    if not thread_info.trace or not thread_info.is_thread_alive():
        # For thread-related stuff we can't disable the code tracing because other
        # threads may still want it...
        return

    frame = _getframe(1)
    func_code_info = _get_func_code_info(code, frame)
    if func_code_info.always_skip_code:
        # if DEBUG:
        #     print('disable (always skip)')
        return monitor.DISABLE

    keep_enabled: bool = _enable_code_tracing(py_db, thread_info.additional_info, func_code_info, code, frame, True)

    if func_code_info.function_breakpoint_found:
        bp = func_code_info.function_breakpoint
        stop = True
        new_frame = frame
        stop_reason = CMD_SET_FUNCTION_BREAK
        stop_on_plugin_breakpoint = False

        _stop_on_breakpoint(py_db, thread_info, stop_reason, bp, frame, new_frame, stop, stop_on_plugin_breakpoint, "python-function")
        return

    if py_db.plugin:
        plugin_manager = py_db.plugin

        # Check breaking on breakpoints in a 'call'
        info = thread_info.additional_info
        if func_code_info.plugin_call_breakpoint_found:
            result = plugin_manager.get_breakpoint(py_db, frame, "call", info)
            if result:
                stop_reason = CMD_SET_BREAK
                stop = False
                stop_on_plugin_breakpoint = True
                bp, new_frame, bp_type = result
                _stop_on_breakpoint(py_db, thread_info, stop_reason, bp, frame, new_frame, stop, stop_on_plugin_breakpoint, bp_type)
                return

            keep_enabled = True

        # Check breaking on line stepping in a 'call'
        step_cmd = info.pydev_step_cmd
        if step_cmd != -1 and func_code_info.plugin_call_stepping and info.suspend_type != PYTHON_SUSPEND:
            _plugin_stepping(py_db, step_cmd, "call", frame, thread_info)
            return

    if keep_enabled or any_thread_stepping():
        return None

    return monitor.DISABLE


# fmt: off
# IFDEF CYTHON
# cpdef _ensure_monitoring():
# ELSE
def _ensure_monitoring():
# ENDIF
# fmt: on
    DEBUGGER_ID = monitor.DEBUGGER_ID
    if not monitor.get_tool(DEBUGGER_ID):
        monitor.use_tool_id(DEBUGGER_ID, "pydevd")
        update_monitor_events()
        restart_events()


# fmt: off
# IFDEF CYTHON
# cpdef start_monitoring(bint all_threads=False):
#     cdef ThreadInfo thread_info
# ELSE
def start_monitoring(all_threads=False):
# ENDIF
# fmt: on
    if all_threads:
        # print('start monitoring, all_threads=', all_threads)
        DEBUGGER_ID = monitor.DEBUGGER_ID
        if not monitor.get_tool(DEBUGGER_ID):
            monitor.use_tool_id(DEBUGGER_ID, "pydevd")
            update_monitor_events()
            restart_events()
    else:
        try:
            thread_info = _thread_local_info.thread_info
        except:
            # code=None means we can already get the threading.current_thread.
            thread_info = _get_thread_info(True, 1)
            if thread_info is None:
                # print('start monitoring, thread=', None)
                return
        # print('start monitoring, thread=', thread_info.thread)
        thread_info.trace = True


# fmt: off
# IFDEF CYTHON
# cpdef stop_monitoring(all_threads=False):
#     cdef ThreadInfo thread_info
# ELSE
def stop_monitoring(all_threads=False):
# ENDIF
# fmt: on
    if all_threads:
        # print('stop monitoring, all_threads=', all_threads)
        if monitor.get_tool(monitor.DEBUGGER_ID) == "pydevd":
            monitor.set_events(monitor.DEBUGGER_ID, 0)
            monitor.register_callback(DEBUGGER_ID, monitor.events.PY_START, None)
            monitor.register_callback(DEBUGGER_ID, monitor.events.PY_RESUME, None)
            monitor.register_callback(DEBUGGER_ID, monitor.events.LINE, None)
            monitor.register_callback(DEBUGGER_ID, monitor.events.JUMP, None)
            monitor.register_callback(DEBUGGER_ID, monitor.events.PY_RETURN, None)
            monitor.register_callback(DEBUGGER_ID, monitor.events.RAISE, None)
            monitor.free_tool_id(monitor.DEBUGGER_ID)
    else:
        try:
            thread_info = _thread_local_info.thread_info
        except:
            thread_info = _get_thread_info(False, 1)
            if thread_info is None:
                return
        # print('stop monitoring, thread=', thread_info.thread)
        thread_info.trace = False


def update_monitor_events(suspend_requested: Optional[bool]=None) -> None:
    """
    This should be called when breakpoints change.

    :param suspend: means the user requested threads to be suspended
    """
    if monitor.get_tool(monitor.DEBUGGER_ID) != "pydevd":
        # It is still not initialized.
        return

    # When breakpoints change we need to update what we want to track based
    # on the breakpoints.
    py_db = GlobalDebuggerHolder.global_dbg
    if py_db is None:
        return

    if suspend_requested is None:
        suspend_requested = False

        for t in threading.enumerate():
            if getattr(t, "pydev_do_not_trace", False):
                continue
            try:
                additional_info = t.additional_info
                if additional_info is None:
                    # i.e.: if we don't have it then it makes no sense to check if it was suspended or is stepping
                    continue
            except AttributeError:
                continue
            if additional_info.pydev_step_cmd != -1 or additional_info.pydev_state == 2:
                suspend_requested = True
                break

    required_events = 0

    has_caught_exception_breakpoint_in_pydb = (
        py_db.break_on_caught_exceptions or py_db.break_on_user_uncaught_exceptions or py_db.has_plugin_exception_breaks
    )

    break_on_uncaught_exceptions = py_db.break_on_uncaught_exceptions

    if has_caught_exception_breakpoint_in_pydb:
        required_events |= monitor.events.RAISE | monitor.events.PY_UNWIND
        # print('track RAISE')
        monitor.register_callback(DEBUGGER_ID, monitor.events.RAISE, _raise_event)
        monitor.register_callback(DEBUGGER_ID, monitor.events.PY_UNWIND, _unwind_event)
    else:
        if break_on_uncaught_exceptions:
            required_events |= monitor.events.PY_UNWIND
            monitor.register_callback(DEBUGGER_ID, monitor.events.PY_UNWIND, _unwind_event)
        else:
            monitor.register_callback(DEBUGGER_ID, monitor.events.RAISE, None)
            monitor.register_callback(DEBUGGER_ID, monitor.events.PY_UNWIND, None)

    has_breaks = py_db.has_plugin_line_breaks
    if not has_breaks:
        if py_db.function_breakpoint_name_to_breakpoint:
            has_breaks = True
        else:
            file_to_line_to_breakpoints = py_db.breakpoints
            for line_to_breakpoints in file_to_line_to_breakpoints.values():
                if line_to_breakpoints:
                    has_breaks = True
                    break

    if has_breaks or suspend_requested:
        # print('track PY_START|PY_RESUME, suspend_requested=', suspend_requested)
        required_events |= monitor.events.PY_START | monitor.events.PY_RESUME

        monitor.register_callback(DEBUGGER_ID, monitor.events.PY_START, _start_method_event)
        # monitor.register_callback(DEBUGGER_ID, monitor.events.PY_RESUME, _resume_method_event)
        monitor.register_callback(DEBUGGER_ID, monitor.events.LINE, _line_event)
        if not IS_PY313_OR_GREATER:
            # In Python 3.13+ jump_events aren't necessary as we have a line_event for every
            # jump location. 
            monitor.register_callback(DEBUGGER_ID, monitor.events.JUMP, _jump_event)
        monitor.register_callback(DEBUGGER_ID, monitor.events.PY_RETURN, _return_event)

    else:
        monitor.register_callback(DEBUGGER_ID, monitor.events.PY_START, None)
        monitor.register_callback(DEBUGGER_ID, monitor.events.PY_RESUME, None)
        monitor.register_callback(DEBUGGER_ID, monitor.events.LINE, None)
        monitor.register_callback(DEBUGGER_ID, monitor.events.JUMP, None)
        monitor.register_callback(DEBUGGER_ID, monitor.events.PY_RETURN, None)

    monitor.set_events(DEBUGGER_ID, required_events)


def restart_events() -> None:
    # Note: if breakpoints change, update_monitor_events usually needs to be
    # called first, then the line event tracing must be set for existing frames
    # and then this function must be called at the end.
    monitor.restart_events()


# fmt: off
# IFDEF CYTHON
# cdef _is_same_frame(PyDBAdditionalThreadInfo info, target_frame, current_frame):
# ELSE
def _is_same_frame(info, target_frame, current_frame):
# ENDIF
# fmt: on
    if target_frame is current_frame:
        return True

    if info.pydev_use_scoped_step_frame:
        # If using scoped step we don't check the target, we just need to check
        # if the current matches the same heuristic where the target was defined.
        if target_frame is not None and current_frame is not None:
            if target_frame.f_code.co_filename == current_frame.f_code.co_filename:
                # The co_name may be different (it may include the line number), but
                # the filename must still be the same.
                f = current_frame.f_back
                if f is not None and f.f_code.co_name == PYDEVD_IPYTHON_CONTEXT[1]:
                    f = f.f_back
                    if f is not None and f.f_code.co_name == PYDEVD_IPYTHON_CONTEXT[2]:
                        return True

    return False


# fmt: off
# IFDEF CYTHON
# def _do_wait_suspend(py_db, ThreadInfo thread_info, frame, event, arg):
# ELSE
def _do_wait_suspend(py_db, thread_info, frame, event, arg):
# ENDIF
# fmt: on
    thread_info.additional_info.trace_suspend_type = "sys_monitor"
    py_db.do_wait_suspend(thread_info.thread, frame, event, arg)

# This can be used to diagnose exceptions inside of the debugger itself.
#
# import types
# import functools
#
#
# def safe_func(method):
#
#     @functools.wraps(method)
#     def new_method(*args, **kwargs):
#         try:
#             return method(*args, **kwargs)
#         except:
#             import traceback;traceback.print_exc()
#             raise
#
#     return new_method
#
#
# for name, obj in list(globals().items()):
#     if name.endswith('_event'):
#         if isinstance(obj, types.FunctionType):
#             globals()[name] = safe_func(obj)
#
#
# def _getframe(depth):
#     return sys._getframe(depth + 1)
