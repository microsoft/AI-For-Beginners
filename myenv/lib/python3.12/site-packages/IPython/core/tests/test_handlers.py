"""Tests for input handlers.
"""
#-----------------------------------------------------------------------------
# Module imports
#-----------------------------------------------------------------------------

# our own packages
from IPython.core import autocall
from IPython.testing import tools as tt
import pytest
from collections.abc import Callable

#-----------------------------------------------------------------------------
# Globals
#-----------------------------------------------------------------------------

# Test functions
#-----------------------------------------------------------------------------

class CallableIndexable(object):
    def __getitem__(self, idx): return True
    def __call__(self, *args, **kws): return True


class Autocallable(autocall.IPyAutocall):
    def __call__(self):
        return "called"


@pytest.mark.parametrize(
    "autocall, input, output",
    [
        # For many of the below, we're also checking that leading whitespace
        # turns off the esc char, which it should unless there is a continuation
        # line.
        ("1", '"no change"', '"no change"'),  # normal
        ("1", "lsmagic", "get_ipython().run_line_magic('lsmagic', '')"),  # magic
        # Only explicit escapes or instances of IPyAutocallable should get
        # expanded
        ("0", 'len "abc"', 'len "abc"'),
        ("0", "autocallable", "autocallable()"),
        # Don't add extra brackets (gh-1117)
        ("0", "autocallable()", "autocallable()"),
        ("1", 'len "abc"', 'len("abc")'),
        ("1", 'len "abc";', 'len("abc");'),  # ; is special -- moves out of parens
        # Autocall is turned off if first arg is [] and the object
        # is both callable and indexable.  Like so:
        ("1", "len [1,2]", "len([1,2])"),  # len doesn't support __getitem__...
        ("1", "call_idx [1]", "call_idx [1]"),  # call_idx *does*..
        ("1", "call_idx 1", "call_idx(1)"),
        ("1", "len", "len"),  # only at 2 does it auto-call on single args
        ("2", 'len "abc"', 'len("abc")'),
        ("2", 'len "abc";', 'len("abc");'),
        ("2", "len [1,2]", "len([1,2])"),
        ("2", "call_idx [1]", "call_idx [1]"),
        ("2", "call_idx 1", "call_idx(1)"),
        # T his is what's different:
        ("2", "len", "len()"),  # only at 2 does it auto-call on single args
        ("0", "Callable[[int], None]", "Callable[[int], None]"),
        ("1", "Callable[[int], None]", "Callable[[int], None]"),
        ("1", "Callable[[int], None]", "Callable[[int], None]"),
    ],
)
def test_handlers_I(autocall, input, output):
    autocallable = Autocallable()
    ip.user_ns["autocallable"] = autocallable

    call_idx = CallableIndexable()
    ip.user_ns["call_idx"] = call_idx

    ip.user_ns["Callable"] = Callable

    ip.run_line_magic("autocall", autocall)
    assert ip.prefilter_manager.prefilter_lines(input) == output
    ip.run_line_magic("autocall", "1")
