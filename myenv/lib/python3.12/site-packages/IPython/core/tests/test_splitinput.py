# coding: utf-8

from IPython.core.splitinput import split_user_input, LineInfo

import pytest

tests = [
    ("x=1", ("", "", "x", "=1")),
    ("?", ("", "?", "", "")),
    ("??", ("", "??", "", "")),
    (" ?", (" ", "?", "", "")),
    (" ??", (" ", "??", "", "")),
    ("??x", ("", "??", "x", "")),
    ("?x=1", ("", "?", "x", "=1")),
    ("!ls", ("", "!", "ls", "")),
    ("  !ls", ("  ", "!", "ls", "")),
    ("!!ls", ("", "!!", "ls", "")),
    ("  !!ls", ("  ", "!!", "ls", "")),
    (",ls", ("", ",", "ls", "")),
    (";ls", ("", ";", "ls", "")),
    ("  ;ls", ("  ", ";", "ls", "")),
    ("f.g(x)", ("", "", "f.g", "(x)")),
    ("f.g (x)", ("", "", "f.g", " (x)")),
    ("?%hist1", ("", "?", "%hist1", "")),
    ("?%%hist2", ("", "?", "%%hist2", "")),
    ("??%hist3", ("", "??", "%hist3", "")),
    ("??%%hist4", ("", "??", "%%hist4", "")),
    ("?x*", ("", "?", "x*", "")),
    ("Pérez Fernando", ("", "", "Pérez", " Fernando")),
]


@pytest.mark.parametrize("input, output", tests)
def test_split_user_input(input, output):
    assert split_user_input(input) == output


def test_LineInfo():
    """Simple test for LineInfo construction and str()"""
    linfo = LineInfo("  %cd /home")
    assert str(linfo) == "LineInfo [  |%|cd|/home]"
