"""Tests for pylab tools module.
"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.


from binascii import a2b_base64
from io import BytesIO

import pytest

matplotlib = pytest.importorskip("matplotlib")
matplotlib.use('Agg')
from matplotlib.figure import Figure

from matplotlib import pyplot as plt
from matplotlib_inline import backend_inline
import numpy as np

from IPython.core.getipython import get_ipython
from IPython.core.interactiveshell import InteractiveShell
from IPython.core.display import _PNG, _JPEG
from .. import pylabtools as pt

from IPython.testing import decorators as dec


def test_figure_to_svg():
    # simple empty-figure test
    fig = plt.figure()
    assert pt.print_figure(fig, "svg") is None

    plt.close('all')

    # simple check for at least svg-looking output
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot([1,2,3])
    plt.draw()
    svg = pt.print_figure(fig, "svg")[:100].lower()
    assert "doctype svg" in svg


def _check_pil_jpeg_bytes():
    """Skip if PIL can't write JPEGs to BytesIO objects"""
    # PIL's JPEG plugin can't write to BytesIO objects
    # Pillow fixes this
    from PIL import Image
    buf = BytesIO()
    img = Image.new("RGB", (4,4))
    try:
        img.save(buf, 'jpeg')
    except Exception as e:
        ename = e.__class__.__name__
        raise pytest.skip("PIL can't write JPEG to BytesIO: %s: %s" % (ename, e)) from e

@dec.skip_without("PIL.Image")
def test_figure_to_jpeg():
    _check_pil_jpeg_bytes()
    # simple check for at least jpeg-looking output
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot([1,2,3])
    plt.draw()
    jpeg = pt.print_figure(fig, 'jpeg', pil_kwargs={'optimize': 50})[:100].lower()
    assert jpeg.startswith(_JPEG)

def test_retina_figure():
    # simple empty-figure test
    fig = plt.figure()
    assert pt.retina_figure(fig) == None
    plt.close('all')

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot([1,2,3])
    plt.draw()
    png, md = pt.retina_figure(fig)
    assert png.startswith(_PNG)
    assert "width" in md
    assert "height" in md


_fmt_mime_map = {
    'png': 'image/png',
    'jpeg': 'image/jpeg',
    'pdf': 'application/pdf',
    'retina': 'image/png',
    'svg': 'image/svg+xml',
}

def test_select_figure_formats_str():
    ip = get_ipython()
    for fmt, active_mime in _fmt_mime_map.items():
        pt.select_figure_formats(ip, fmt)
        for mime, f in ip.display_formatter.formatters.items():
            if mime == active_mime:
                assert Figure in f
            else:
                assert Figure not in f

def test_select_figure_formats_kwargs():
    ip = get_ipython()
    kwargs = dict(bbox_inches="tight")
    pt.select_figure_formats(ip, "png", **kwargs)
    formatter = ip.display_formatter.formatters["image/png"]
    f = formatter.lookup_by_type(Figure)
    cell = f.keywords
    expected = kwargs
    expected["base64"] = True
    expected["fmt"] = "png"
    assert cell == expected

    # check that the formatter doesn't raise
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot([1,2,3])
    plt.draw()
    formatter.enabled = True
    png = formatter(fig)
    assert isinstance(png, str)
    png_bytes = a2b_base64(png)
    assert png_bytes.startswith(_PNG)

def test_select_figure_formats_set():
    ip = get_ipython()
    for fmts in [
        {'png', 'svg'},
        ['png'],
        ('jpeg', 'pdf', 'retina'),
        {'svg'},
    ]:
        active_mimes = {_fmt_mime_map[fmt] for fmt in fmts}
        pt.select_figure_formats(ip, fmts)
        for mime, f in ip.display_formatter.formatters.items():
            if mime in active_mimes:
                assert Figure in f
            else:
                assert Figure not in f

def test_select_figure_formats_bad():
    ip = get_ipython()
    with pytest.raises(ValueError):
        pt.select_figure_formats(ip, 'foo')
    with pytest.raises(ValueError):
        pt.select_figure_formats(ip, {'png', 'foo'})
    with pytest.raises(ValueError):
        pt.select_figure_formats(ip, ['retina', 'pdf', 'bar', 'bad'])

def test_import_pylab():
    ns = {}
    pt.import_pylab(ns, import_all=False)
    assert "plt" in ns
    assert ns["np"] == np


class TestPylabSwitch(object):
    class Shell(InteractiveShell):
        def init_history(self):
            """Sets up the command history, and starts regular autosaves."""
            self.config.HistoryManager.hist_file = ":memory:"
            super().init_history()

        def enable_gui(self, gui):
            pass

    def setup_method(self):
        import matplotlib
        def act_mpl(backend):
            matplotlib.rcParams['backend'] = backend

        # Save rcParams since they get modified
        self._saved_rcParams = matplotlib.rcParams
        self._saved_rcParamsOrig = matplotlib.rcParamsOrig
        matplotlib.rcParams = dict(backend="QtAgg")
        matplotlib.rcParamsOrig = dict(backend="QtAgg")

        # Mock out functions
        self._save_am = pt.activate_matplotlib
        pt.activate_matplotlib = act_mpl
        self._save_ip = pt.import_pylab
        pt.import_pylab = lambda *a,**kw:None
        self._save_cis = backend_inline.configure_inline_support
        backend_inline.configure_inline_support = lambda *a, **kw: None

    def teardown_method(self):
        pt.activate_matplotlib = self._save_am
        pt.import_pylab = self._save_ip
        backend_inline.configure_inline_support = self._save_cis
        import matplotlib
        matplotlib.rcParams = self._saved_rcParams
        matplotlib.rcParamsOrig = self._saved_rcParamsOrig

    def test_qt(self):
        s = self.Shell()
        gui, backend = s.enable_matplotlib(None)
        assert gui == "qt"
        assert s.pylab_gui_select == "qt"

        gui, backend = s.enable_matplotlib("inline")
        assert gui is None
        assert s.pylab_gui_select == "qt"

        gui, backend = s.enable_matplotlib("qt")
        assert gui == "qt"
        assert s.pylab_gui_select == "qt"

        gui, backend = s.enable_matplotlib("inline")
        assert gui is None
        assert s.pylab_gui_select == "qt"

        gui, backend = s.enable_matplotlib()
        assert gui == "qt"
        assert s.pylab_gui_select == "qt"

    def test_inline(self):
        s = self.Shell()
        gui, backend = s.enable_matplotlib("inline")
        assert gui is None
        assert s.pylab_gui_select == None

        gui, backend = s.enable_matplotlib("inline")
        assert gui is None
        assert s.pylab_gui_select == None

        gui, backend = s.enable_matplotlib("qt")
        assert gui == "qt"
        assert s.pylab_gui_select == "qt"

    def test_inline_twice(self):
        "Using '%matplotlib inline' twice should not reset formatters"

        ip = self.Shell()
        gui, backend = ip.enable_matplotlib("inline")
        assert gui is None

        fmts =  {'png'}
        active_mimes = {_fmt_mime_map[fmt] for fmt in fmts}
        pt.select_figure_formats(ip, fmts)

        gui, backend = ip.enable_matplotlib("inline")
        assert gui is None

        for mime, f in ip.display_formatter.formatters.items():
            if mime in active_mimes:
                assert Figure in f
            else:
                assert Figure not in f

    def test_qt_gtk(self):
        s = self.Shell()
        gui, backend = s.enable_matplotlib("qt")
        assert gui == "qt"
        assert s.pylab_gui_select == "qt"

        gui, backend = s.enable_matplotlib("gtk3")
        assert gui == "qt"
        assert s.pylab_gui_select == "qt"

    @dec.skipif(not pt._matplotlib_manages_backends())
    def test_backend_module_name_case_sensitive(self):
        # Matplotlib backend names are case insensitive unless explicitly specified using
        # "module://some_module.some_name" syntax which are case sensitive for mpl >= 3.9.1
        all_lowercase = "module://matplotlib_inline.backend_inline"
        some_uppercase = "module://matplotlib_inline.Backend_inline"
        mpl3_9_1 = matplotlib.__version_info__ >= (3, 9, 1)

        s = self.Shell()
        s.enable_matplotlib(all_lowercase)
        if mpl3_9_1:
            with pytest.raises(RuntimeError):
                s.enable_matplotlib(some_uppercase)
        else:
            s.enable_matplotlib(some_uppercase)

        s.run_line_magic("matplotlib", all_lowercase)
        if mpl3_9_1:
            with pytest.raises(RuntimeError):
                s.run_line_magic("matplotlib", some_uppercase)
        else:
            s.run_line_magic("matplotlib", some_uppercase)


def test_no_gui_backends():
    for k in ['agg', 'svg', 'pdf', 'ps']:
        assert k not in pt.backend2gui


def test_figure_no_canvas():
    fig = Figure()
    fig.canvas = None
    pt.print_figure(fig)


@pytest.mark.parametrize(
    "name, expected_gui, expected_backend",
    [
        # name is gui
        ("gtk3", "gtk3", "gtk3agg"),
        ("gtk4", "gtk4", "gtk4agg"),
        ("headless", None, "agg"),
        ("osx", "osx", "macosx"),
        ("qt", "qt", "qtagg"),
        ("qt5", "qt5", "qt5agg"),
        ("qt6", "qt6", "qtagg"),
        ("tk", "tk", "tkagg"),
        ("wx", "wx", "wxagg"),
        # name is backend
        ("agg", None, "agg"),
        ("cairo", None, "cairo"),
        ("pdf", None, "pdf"),
        ("ps", None, "ps"),
        ("svg", None, "svg"),
        ("template", None, "template"),
        ("gtk3agg", "gtk3", "gtk3agg"),
        ("gtk3cairo", "gtk3", "gtk3cairo"),
        ("gtk4agg", "gtk4", "gtk4agg"),
        ("gtk4cairo", "gtk4", "gtk4cairo"),
        ("macosx", "osx", "macosx"),
        ("nbagg", "nbagg", "nbagg"),
        ("notebook", "nbagg", "notebook"),
        ("qtagg", "qt", "qtagg"),
        ("qtcairo", "qt", "qtcairo"),
        ("qt5agg", "qt5", "qt5agg"),
        ("qt5cairo", "qt5", "qt5cairo"),
        ("tkagg", "tk", "tkagg"),
        ("tkcairo", "tk", "tkcairo"),
        ("webagg", "webagg", "webagg"),
        ("wxagg", "wx", "wxagg"),
        ("wxcairo", "wx", "wxcairo"),
    ],
)
def test_backend_builtin(name, expected_gui, expected_backend):
    # Test correct identification of Matplotlib built-in backends without importing and using them,
    # otherwise we would need to ensure all the complex dependencies such as windowing toolkits are
    # installed.

    mpl_manages_backends = pt._matplotlib_manages_backends()
    if not mpl_manages_backends:
        # Backends not supported before _matplotlib_manages_backends or supported
        # but with different expected_gui or expected_backend.
        if (
            name.endswith("agg")
            or name.endswith("cairo")
            or name in ("headless", "macosx", "pdf", "ps", "svg", "template")
        ):
            pytest.skip()
        elif name == "qt6":
            expected_backend = "qtagg"
        elif name == "notebook":
            expected_backend, expected_gui = expected_gui, expected_backend

    gui, backend = pt.find_gui_and_backend(name)
    if not mpl_manages_backends:
        gui = gui.lower() if gui else None
        backend = backend.lower() if backend else None
    assert gui == expected_gui
    assert backend == expected_backend


def test_backend_entry_point():
    gui, backend = pt.find_gui_and_backend("inline")
    assert gui is None
    expected_backend = (
        "inline"
        if pt._matplotlib_manages_backends()
        else "module://matplotlib_inline.backend_inline"
    )
    assert backend == expected_backend


def test_backend_unknown():
    with pytest.raises(RuntimeError if pt._matplotlib_manages_backends() else KeyError):
        pt.find_gui_and_backend("name-does-not-exist")
