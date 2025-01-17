"""Python bindings for 0MQ"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

from __future__ import annotations

import os
import sys
from contextlib import contextmanager


@contextmanager
def _libs_on_path():
    """context manager for libs directory on $PATH

    Works around mysterious issue where os.add_dll_directory
    does not resolve imports (conda-forge Python >= 3.8)
    """

    if not sys.platform.startswith("win"):
        yield
        return

    libs_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            os.pardir,
            "pyzmq.libs",
        )
    )
    if not os.path.exists(libs_dir):
        # no bundled libs
        yield
        return

    path_before = os.environ.get("PATH")
    try:
        os.environ["PATH"] = os.pathsep.join([path_before or "", libs_dir])
        yield
    finally:
        if path_before is None:
            os.environ.pop("PATH")
        else:
            os.environ["PATH"] = path_before


# zmq top-level imports

# workaround for Windows
with _libs_on_path():
    from zmq import backend

from . import constants  # noqa
from .constants import *  # noqa
from zmq.backend import *  # noqa
from zmq import sugar
from zmq.sugar import *  # noqa


def get_includes():
    """Return a list of directories to include for linking against pyzmq with cython."""
    from os.path import abspath, dirname, exists, join, pardir

    base = dirname(__file__)
    parent = abspath(join(base, pardir))
    includes = [parent] + [join(parent, base, subdir) for subdir in ('utils',)]
    if exists(join(parent, base, 'include')):
        includes.append(join(parent, base, 'include'))
    return includes


def get_library_dirs():
    """Return a list of directories used to link against pyzmq's bundled libzmq."""
    from os.path import abspath, dirname, join, pardir

    base = dirname(__file__)
    parent = abspath(join(base, pardir))
    return [join(parent, base)]


COPY_THRESHOLD = 65536
DRAFT_API = backend.has("draft")

__all__ = (
    [
        'get_includes',
        'COPY_THRESHOLD',
        'DRAFT_API',
    ]
    + constants.__all__
    + sugar.__all__
    + backend.__all__
)
