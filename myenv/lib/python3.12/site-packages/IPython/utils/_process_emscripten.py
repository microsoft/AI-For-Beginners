"""Emscripten-specific implementation of process utilities.

This file is only meant to be imported by process.py, not by end-users.
"""

from ._process_common import arg_split


def system(cmd):
    raise OSError("Not available")


def getoutput(cmd):
    raise OSError("Not available")


def check_pid(cmd):
    raise OSError("Not available")


# `arg_split` is still used by magics regardless of whether we are on a posix/windows/emscipten
__all__ = ["system", "getoutput", "check_pid", "arg_split"]
