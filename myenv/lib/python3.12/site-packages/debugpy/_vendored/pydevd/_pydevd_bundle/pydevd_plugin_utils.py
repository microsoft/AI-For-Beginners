import types

from _pydev_bundle import pydev_log
from typing import Tuple, Literal

try:
    from pydevd_plugins import django_debug
except:
    django_debug = None
    pydev_log.debug("Unable to load django_debug plugin")

try:
    from pydevd_plugins import jinja2_debug
except:
    jinja2_debug = None
    pydev_log.debug("Unable to load jinja2_debug plugin")


def load_plugins():
    plugins = []
    if django_debug is not None:
        plugins.append(django_debug)

    if jinja2_debug is not None:
        plugins.append(jinja2_debug)
    return plugins


def bind_func_to_method(func, obj, method_name):
    bound_method = types.MethodType(func, obj)

    setattr(obj, method_name, bound_method)
    return bound_method


class PluginManager(object):
    EMPTY_SENTINEL = object()

    def __init__(self, main_debugger):
        self.plugins = load_plugins()

        # When some breakpoint is added for a given plugin it becomes active.
        self.active_plugins = []

        self.main_debugger = main_debugger

    def add_breakpoint(self, func_name, *args, **kwargs):
        # add breakpoint for plugin
        for plugin in self.plugins:
            if hasattr(plugin, func_name):
                func = getattr(plugin, func_name)
                result = func(*args, **kwargs)
                if result:
                    self.activate(plugin)
                    return result
        return None

    def activate(self, plugin):
        if plugin not in self.active_plugins:
            self.active_plugins.append(plugin)

    # These are not a part of the API, rather, `add_breakpoint` should be used with `add_line_breakpoint` or `add_exception_breakpoint`
    # which will call it for all plugins and then if it's valid it'll be activated.
    #
    # def add_line_breakpoint(self, py_db, type, canonical_normalized_filename, breakpoint_id, line, condition, expression, func_name, hit_condition=None, is_logpoint=False, add_breakpoint_result=None, on_changed_breakpoint_state=None):
    # def add_exception_breakpoint(plugin, py_db, type, exception):

    def after_breakpoints_consolidated(self, py_db, canonical_normalized_filename, id_to_pybreakpoint, file_to_line_to_breakpoints):
        for plugin in self.active_plugins:
            plugin.after_breakpoints_consolidated(py_db, canonical_normalized_filename, id_to_pybreakpoint, file_to_line_to_breakpoints)

    def remove_exception_breakpoint(self, py_db, exception_type, exception):
        """
        :param exception_type: 'django', 'jinja2' (can be extended)
        """
        for plugin in self.active_plugins:
            ret = plugin.remove_exception_breakpoint(py_db, exception_type, exception)
            if ret:
                return ret

        return None

    def remove_all_exception_breakpoints(self, py_db):
        for plugin in self.active_plugins:
            plugin.remove_all_exception_breakpoints(py_db)

    def get_breakpoints(self, py_db, breakpoint_type):
        """
        :param breakpoint_type: 'django-line', 'jinja2-line'
        """
        for plugin in self.active_plugins:
            ret = plugin.get_breakpoints(py_db, breakpoint_type)
            if ret:
                return ret

    def can_skip(self, py_db, frame):
        for plugin in self.active_plugins:
            if not plugin.can_skip(py_db, frame):
                return False
        return True

    def required_events_breakpoint(self) -> Tuple[Literal["line", "call"], ...]:
        ret = ()
        for plugin in self.active_plugins:
            new = plugin.required_events_breakpoint()
            if new:
                ret += new

        return ret

    def required_events_stepping(self) -> Tuple[Literal["line", "call", "return"], ...]:
        ret = ()
        for plugin in self.active_plugins:
            new = plugin.required_events_stepping()
            if new:
                ret += new

        return ret

    def is_tracked_frame(self, frame) -> bool:
        for plugin in self.active_plugins:
            if plugin.is_tracked_frame(frame):
                return True
        return False

    def has_exception_breaks(self, py_db) -> bool:
        for plugin in self.active_plugins:
            if plugin.has_exception_breaks(py_db):
                return True
        return False

    def has_line_breaks(self, py_db) -> bool:
        for plugin in self.active_plugins:
            if plugin.has_line_breaks(py_db):
                return True
        return False

    def cmd_step_into(self, py_db, frame, event, info, thread, stop_info, stop: bool):
        """
        :param stop_info: in/out information. If it should stop then it'll be
            filled by the plugin.
        :param stop: whether the stop has already been flagged for this frame.
        :returns:
            tuple(stop, plugin_stop)
        """
        plugin_stop = False
        for plugin in self.active_plugins:
            stop, plugin_stop = plugin.cmd_step_into(py_db, frame, event, info, thread, stop_info, stop)
            if plugin_stop:
                return stop, plugin_stop
        return stop, plugin_stop

    def cmd_step_over(self, py_db, frame, event, info, thread, stop_info, stop):
        plugin_stop = False
        for plugin in self.active_plugins:
            stop, plugin_stop = plugin.cmd_step_over(py_db, frame, event, info, thread, stop_info, stop)
            if plugin_stop:
                return stop, plugin_stop
        return stop, plugin_stop

    def stop(self, py_db, frame, event, thread, stop_info, arg, step_cmd):
        """
        The way this works is that the `cmd_step_into` or `cmd_step_over`
        is called which then fills the `stop_info` and then this method
        is called to do the actual stop.
        """
        for plugin in self.active_plugins:
            stopped = plugin.stop(py_db, frame, event, thread, stop_info, arg, step_cmd)
            if stopped:
                return stopped
        return False

    def get_breakpoint(self, py_db, frame, event, info):
        for plugin in self.active_plugins:
            ret = plugin.get_breakpoint(py_db, frame, event, info)
            if ret:
                return ret
        return None

    def suspend(self, py_db, thread, frame, bp_type):
        """
        :param bp_type: 'django' or 'jinja2'

        :return:
            The frame for the suspend or None if it should not be suspended.
        """
        for plugin in self.active_plugins:
            ret = plugin.suspend(py_db, thread, frame, bp_type)
            if ret is not None:
                return ret

        return None

    def exception_break(self, py_db, frame, thread, arg, is_unwind=False):
        for plugin in self.active_plugins:
            ret = plugin.exception_break(py_db, frame, thread, arg, is_unwind)
            if ret is not None:
                return ret

        return None

    def change_variable(self, frame, attr, expression):
        for plugin in self.active_plugins:
            ret = plugin.change_variable(frame, attr, expression, self.EMPTY_SENTINEL)
            if ret is not self.EMPTY_SENTINEL:
                return ret

        return self.EMPTY_SENTINEL
