"""
Watchers are loggers that log detailed information on
CLIPS, disabled by default and that can be enabled by
the `(watch)` method.

Here, we expose a rule, fact and agenda watchers as
well as a method to enable/disable them both individually
and all of them.

"""
import logging

__all__ = ['watch', 'unwatch']

logging.basicConfig()


def define_watcher(name):
    return logging.getLogger('.'.join((__name__, name)))


def worth(what, level_name):
    """Returns `True` if the watcher `what` would log under `level_name`."""
    return (logging.NOTSET
            < globals()[what].level
            <= getattr(logging, level_name))


def watch(*what, level=logging.DEBUG):
    """
    Enable watchers.

    Defaults to enable all watchers, accepts a list names of watchers to
    enable.

    """
    if not what:
        what = ALL

    for watcher_name in what:
        watcher = globals()[watcher_name]
        watcher.setLevel(level)


def unwatch(*what):
    """
    Disable watchers.

    Defaults to enable all watchers, accepts a list names of watchers to
    enable.

    """
    watch(*what, level=logging.CRITICAL)


RULES = define_watcher('RULES')
ACTIVATIONS = define_watcher('ACTIVATIONS')
FACTS = define_watcher('FACTS')
AGENDA = define_watcher('AGENDA')
MATCH = define_watcher('MATCH')
MATCHER = define_watcher('MATCHER')
ENGINE = define_watcher('ENGINE')

ALL = tuple(k for k in globals() if k.isupper() and k != 'ALL')
