"""pure Python monitored_queue function

For use when Cython extension is unavailable (PyPy).

Authors
-------
* MinRK
"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

from typing import Callable

import zmq
from zmq.backend import monitored_queue as _backend_mq


def _relay(ins, outs, sides, prefix, swap_ids):
    msg = ins.recv_multipart()
    if swap_ids:
        msg[:2] = msg[:2][::-1]
    outs.send_multipart(msg)
    sides.send_multipart([prefix] + msg)


def _monitored_queue(
    in_socket, out_socket, mon_socket, in_prefix=b'in', out_prefix=b'out'
):
    swap_ids = in_socket.type == zmq.ROUTER and out_socket.type == zmq.ROUTER

    poller = zmq.Poller()
    poller.register(in_socket, zmq.POLLIN)
    poller.register(out_socket, zmq.POLLIN)
    while True:
        events = dict(poller.poll())
        if in_socket in events:
            _relay(in_socket, out_socket, mon_socket, in_prefix, swap_ids)
        if out_socket in events:
            _relay(out_socket, in_socket, mon_socket, out_prefix, swap_ids)


monitored_queue: Callable
if _backend_mq is not None:
    monitored_queue = _backend_mq  # type: ignore
else:
    # backend has no monitored_queue
    monitored_queue = _monitored_queue


__all__ = ['monitored_queue']
