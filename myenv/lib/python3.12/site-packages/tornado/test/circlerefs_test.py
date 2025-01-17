"""Test script to find circular references.

Circular references are not leaks per se, because they will eventually
be GC'd. However, on CPython, they prevent the reference-counting fast
path from being used and instead rely on the slower full GC. This
increases memory footprint and CPU overhead, so we try to eliminate
circular references created by normal operation.
"""

import asyncio
import contextlib
import gc
import io
import sys
import traceback
import types
import typing
import unittest

import tornado
from tornado import web, gen, httpclient
from tornado.test.util import skipNotCPython


def find_circular_references(garbage):
    """Find circular references in a list of objects.

    The garbage list contains objects that participate in a cycle,
    but also the larger set of objects kept alive by that cycle.
    This function finds subsets of those objects that make up
    the cycle(s).
    """

    def inner(level):
        for item in level:
            item_id = id(item)
            if item_id not in garbage_ids:
                continue
            if item_id in visited_ids:
                continue
            if item_id in stack_ids:
                candidate = stack[stack.index(item) :]
                candidate.append(item)
                found.append(candidate)
                continue

            stack.append(item)
            stack_ids.add(item_id)
            inner(gc.get_referents(item))
            stack.pop()
            stack_ids.remove(item_id)
            visited_ids.add(item_id)

    found: typing.List[object] = []
    stack = []
    stack_ids = set()
    garbage_ids = set(map(id, garbage))
    visited_ids = set()

    inner(garbage)
    return found


@contextlib.contextmanager
def assert_no_cycle_garbage():
    """Raise AssertionError if the wrapped code creates garbage with cycles."""
    gc.disable()
    gc.collect()
    gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_SAVEALL)
    yield
    try:
        # We have DEBUG_STATS on which causes gc.collect to write to stderr.
        # Capture the output instead of spamming the logs on passing runs.
        f = io.StringIO()
        old_stderr = sys.stderr
        sys.stderr = f
        try:
            gc.collect()
        finally:
            sys.stderr = old_stderr
        garbage = gc.garbage[:]
        # Must clear gc.garbage (the same object, not just replacing it with a
        # new list) to avoid warnings at shutdown.
        gc.garbage[:] = []
        if len(garbage) == 0:
            return
        for circular in find_circular_references(garbage):
            f.write("\n==========\n Circular \n==========")
            for item in circular:
                f.write(f"\n    {repr(item)}")
            for item in circular:
                if isinstance(item, types.FrameType):
                    f.write(f"\nLocals: {item.f_locals}")
                    f.write(f"\nTraceback: {repr(item)}")
                    traceback.print_stack(item)
        del garbage
        raise AssertionError(f.getvalue())
    finally:
        gc.set_debug(0)
        gc.enable()


# GC behavior is cpython-specific
@skipNotCPython
class CircleRefsTest(unittest.TestCase):
    def test_known_leak(self):
        # Construct a known leak scenario to make sure the test harness works.
        class C(object):
            def __init__(self, name):
                self.name = name
                self.a: typing.Optional[C] = None
                self.b: typing.Optional[C] = None
                self.c: typing.Optional[C] = None

            def __repr__(self):
                return f"name={self.name}"

        with self.assertRaises(AssertionError) as cm:
            with assert_no_cycle_garbage():
                # a and b form a reference cycle. c is not part of the cycle,
                # but it cannot be GC'd while a and b are alive.
                a = C("a")
                b = C("b")
                c = C("c")
                a.b = b
                a.c = c
                b.a = a
                b.c = c
                del a, b
        self.assertIn("Circular", str(cm.exception))
        # Leading spaces ensure we only catch these at the beginning of a line, meaning they are a
        # cycle participant and not simply the contents of a locals dict or similar container. (This
        # depends on the formatting above which isn't ideal but this test evolved from a
        # command-line script) Note that the behavior here changed in python 3.11; in newer pythons
        # locals are handled a bit differently and the test passes without the spaces.
        self.assertIn("    name=a", str(cm.exception))
        self.assertIn("    name=b", str(cm.exception))
        self.assertNotIn("    name=c", str(cm.exception))

    async def run_handler(self, handler_class):
        app = web.Application(
            [
                (r"/", handler_class),
            ]
        )
        socket, port = tornado.testing.bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(socket)

        client = httpclient.AsyncHTTPClient()
        with assert_no_cycle_garbage():
            # Only the fetch (and the corresponding server-side handler)
            # are being tested for cycles. In particular, the Application
            # object has internal cycles (as of this writing) which we don't
            # care to fix since in real world usage the Application object
            # is effectively a global singleton.
            await client.fetch(f"http://127.0.0.1:{port}/")
        client.close()
        server.stop()
        socket.close()

    def test_sync_handler(self):
        class Handler(web.RequestHandler):
            def get(self):
                self.write("ok\n")

        asyncio.run(self.run_handler(Handler))

    def test_finish_exception_handler(self):
        class Handler(web.RequestHandler):
            def get(self):
                raise web.Finish("ok\n")

        asyncio.run(self.run_handler(Handler))

    def test_coro_handler(self):
        class Handler(web.RequestHandler):
            @gen.coroutine
            def get(self):
                yield asyncio.sleep(0.01)
                self.write("ok\n")

        asyncio.run(self.run_handler(Handler))

    def test_async_handler(self):
        class Handler(web.RequestHandler):
            async def get(self):
                await asyncio.sleep(0.01)
                self.write("ok\n")

        asyncio.run(self.run_handler(Handler))

    def test_run_on_executor(self):
        # From https://github.com/tornadoweb/tornado/issues/2620
        #
        # When this test was introduced it found cycles in IOLoop.add_future
        # and tornado.concurrent.chain_future.
        import concurrent.futures

        with concurrent.futures.ThreadPoolExecutor(1) as thread_pool:

            class Factory(object):
                executor = thread_pool

                @tornado.concurrent.run_on_executor
                def run(self):
                    return None

            factory = Factory()

            async def main():
                # The cycle is not reported on the first call. It's not clear why.
                for i in range(2):
                    await factory.run()

            with assert_no_cycle_garbage():
                asyncio.run(main())
