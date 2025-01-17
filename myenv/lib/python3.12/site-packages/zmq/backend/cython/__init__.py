"""Python bindings for core 0MQ objects."""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

from . import _zmq

# mq not in __all__
from ._zmq import *  # noqa
from ._zmq import monitored_queue  # noqa

Message = _zmq.Frame

__all__ = ["Message"]
__all__.extend(_zmq.__all__)
