"""Implementation of coroutines using ``async def``/``await`` keywords.

These keywords replaced ``@asyncio.coroutine`` and ``yield from`` from
Python 3.5 onwards.
"""
import asyncio
import errno
import signal
from sys import version_info as py_version_info

from pexpect import EOF

if py_version_info >= (3, 7):
    # get_running_loop, new in 3.7, is preferred to get_event_loop
    _loop_getter = asyncio.get_running_loop
else:
    # Deprecation warning since 3.10
    _loop_getter = asyncio.get_event_loop


async def expect_async(expecter, timeout=None):
    # First process data that was previously read - if it maches, we don't need
    # async stuff.
    idx = expecter.existing_data()
    if idx is not None:
        return idx
    if not expecter.spawn.async_pw_transport:
        pattern_waiter = PatternWaiter()
        pattern_waiter.set_expecter(expecter)
        transport, pattern_waiter = await _loop_getter().connect_read_pipe(
            lambda: pattern_waiter, expecter.spawn
        )
        expecter.spawn.async_pw_transport = pattern_waiter, transport
    else:
        pattern_waiter, transport = expecter.spawn.async_pw_transport
        pattern_waiter.set_expecter(expecter)
        transport.resume_reading()
    try:
        return await asyncio.wait_for(pattern_waiter.fut, timeout)
    except asyncio.TimeoutError as exc:
        transport.pause_reading()
        return expecter.timeout(exc)


async def repl_run_command_async(repl, cmdlines, timeout=-1):
    res = []
    repl.child.sendline(cmdlines[0])
    for line in cmdlines[1:]:
        await repl._expect_prompt(timeout=timeout, async_=True)
        res.append(repl.child.before)
        repl.child.sendline(line)

    # Command was fully submitted, now wait for the next prompt
    prompt_idx = await repl._expect_prompt(timeout=timeout, async_=True)
    if prompt_idx == 1:
        # We got the continuation prompt - command was incomplete
        repl.child.kill(signal.SIGINT)
        await repl._expect_prompt(timeout=1, async_=True)
        raise ValueError("Continuation prompt found - input was incomplete:")
    return "".join(res + [repl.child.before])


class PatternWaiter(asyncio.Protocol):
    transport = None

    def set_expecter(self, expecter):
        self.expecter = expecter
        self.fut = asyncio.Future()

    def found(self, result):
        if not self.fut.done():
            self.fut.set_result(result)
            self.transport.pause_reading()

    def error(self, exc):
        if not self.fut.done():
            self.fut.set_exception(exc)
            self.transport.pause_reading()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        spawn = self.expecter.spawn
        s = spawn._decoder.decode(data)
        spawn._log(s, "read")

        if self.fut.done():
            spawn._before.write(s)
            spawn._buffer.write(s)
            return

        try:
            index = self.expecter.new_data(s)
            if index is not None:
                # Found a match
                self.found(index)
        except Exception as exc:
            self.expecter.errored()
            self.error(exc)

    def eof_received(self):
        # N.B. If this gets called, async will close the pipe (the spawn object)
        # for us
        try:
            self.expecter.spawn.flag_eof = True
            index = self.expecter.eof()
        except EOF as exc:
            self.error(exc)
        else:
            self.found(index)

    def connection_lost(self, exc):
        if isinstance(exc, OSError) and exc.errno == errno.EIO:
            # We may get here without eof_received being called, e.g on Linux
            self.eof_received()
        elif exc is not None:
            self.error(exc)
