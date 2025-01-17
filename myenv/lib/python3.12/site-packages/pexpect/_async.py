"""Facade that provides coroutines implementation pertinent to running Py version.

Python 3.5 introduced the async def/await syntax keyword.
With later versions coroutines and methods to get the running asyncio loop are
being deprecated, not supported anymore.

For Python versions later than 3.6, coroutines and objects that are defined via
``async def``/``await`` keywords are imported.

Here the code is just imported, to provide the same interface to older code.
"""
# pylint: disable=unused-import
# flake8: noqa: F401
from sys import version_info as py_version_info

# this assumes async def/await are more stable
if py_version_info >= (3, 6):
    from pexpect._async_w_await import (
        PatternWaiter,
        expect_async,
        repl_run_command_async,
    )
else:
    from pexpect._async_pre_await import (
        PatternWaiter,
        expect_async,
        repl_run_command_async,
    )
