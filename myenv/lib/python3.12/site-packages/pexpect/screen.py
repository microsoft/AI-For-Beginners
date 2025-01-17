'''This implements a virtual screen. This is used to support ANSI terminal
emulation. The screen representation and state is implemented in this class.
Most of the methods are inspired by ANSI screen control codes. The
:class:`~pexpect.ANSI.ANSI` class extends this class to add parsing of ANSI
escape codes.

PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2012, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

'''

import codecs
import copy
import sys

import warnings

warnings.warn(("pexpect.screen and pexpect.ANSI are deprecated. "
               "We recommend using pyte to emulate a terminal screen: "
               "https://pypi.python.org/pypi/pyte"),
               stacklevel=2)

NUL = 0    # Fill character; ignored on input.
ENQ = 5    # Transmit answerback message.
BEL = 7    # Ring the bell.
BS  = 8    # Move cursor left.
HT  = 9    # Move cursor to next tab stop.
LF = 10    # Line feed.
VT = 11    # Same as LF.
FF = 12    # Same as LF.
CR = 13    # Move cursor to left margin or newline.
SO = 14    # Invoke G1 character set.
SI = 15    # Invoke G0 character set.
XON = 17   # Resume transmission.
XOFF = 19  # Halt transmission.
CAN = 24   # Cancel escape sequence.
SUB = 26   # Same as CAN.
ESC = 27   # Introduce a control sequence.
DEL = 127  # Fill character; ignored on input.
SPACE = u' ' # Space or blank character.

PY3 = (sys.version_info[0] >= 3)
if PY3:
    unicode = str

def constrain (n, min, max):

    '''This returns a number, n constrained to the min and max bounds. '''

    if n < min:
        return min
    if n > max:
        return max
    return n

class screen:
    '''This object maintains the state of a virtual text screen as a
    rectangular array. This maintains a virtual cursor position and handles
    scrolling as characters are added. This supports most of the methods needed
    by an ANSI text screen. Row and column indexes are 1-based (not zero-based,
    like arrays).

    Characters are represented internally using unicode. Methods that accept
    input characters, when passed 'bytes' (which in Python 2 is equivalent to
    'str'), convert them from the encoding specified in the 'encoding'
    parameter to the constructor. Methods that return screen contents return
    unicode strings, with the exception of __str__() under Python 2. Passing
    ``encoding=None`` limits the API to only accept unicode input, so passing
    bytes in will raise :exc:`TypeError`.
    '''
    def __init__(self, r=24, c=80, encoding='latin-1', encoding_errors='replace'):
        '''This initializes a blank screen of the given dimensions.'''

        self.rows = r
        self.cols = c
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        if encoding is not None:
            self.decoder = codecs.getincrementaldecoder(encoding)(encoding_errors)
        else:
            self.decoder = None
        self.cur_r = 1
        self.cur_c = 1
        self.cur_saved_r = 1
        self.cur_saved_c = 1
        self.scroll_row_start = 1
        self.scroll_row_end = self.rows
        self.w = [ [SPACE] * self.cols for _ in range(self.rows)]

    def _decode(self, s):
        '''This converts from the external coding system (as passed to
        the constructor) to the internal one (unicode). '''
        if self.decoder is not None:
            return self.decoder.decode(s)
        else:
            raise TypeError("This screen was constructed with encoding=None, "
                            "so it does not handle bytes.")

    def _unicode(self):
        '''This returns a printable representation of the screen as a unicode
        string (which, under Python 3.x, is the same as 'str'). The end of each
        screen line is terminated by a newline.'''

        return u'\n'.join ([ u''.join(c) for c in self.w ])

    if PY3:
        __str__ = _unicode
    else:
        __unicode__ = _unicode

        def __str__(self):
            '''This returns a printable representation of the screen. The end of
            each screen line is terminated by a newline. '''
            encoding = self.encoding or 'ascii'
            return self._unicode().encode(encoding, 'replace')

    def dump (self):
        '''This returns a copy of the screen as a unicode string. This is similar to
        __str__/__unicode__ except that lines are not terminated with line
        feeds.'''

        return u''.join ([ u''.join(c) for c in self.w ])

    def pretty (self):
        '''This returns a copy of the screen as a unicode string with an ASCII
        text box around the screen border. This is similar to
        __str__/__unicode__ except that it adds a box.'''

        top_bot = u'+' + u'-'*self.cols + u'+\n'
        return top_bot + u'\n'.join([u'|'+line+u'|' for line in unicode(self).split(u'\n')]) + u'\n' + top_bot

    def fill (self, ch=SPACE):

        if isinstance(ch, bytes):
            ch = self._decode(ch)

        self.fill_region (1,1,self.rows,self.cols, ch)

    def fill_region (self, rs,cs, re,ce, ch=SPACE):

        if isinstance(ch, bytes):
            ch = self._decode(ch)

        rs = constrain (rs, 1, self.rows)
        re = constrain (re, 1, self.rows)
        cs = constrain (cs, 1, self.cols)
        ce = constrain (ce, 1, self.cols)
        if rs > re:
            rs, re = re, rs
        if cs > ce:
            cs, ce = ce, cs
        for r in range (rs, re+1):
            for c in range (cs, ce + 1):
                self.put_abs (r,c,ch)

    def cr (self):
        '''This moves the cursor to the beginning (col 1) of the current row.
        '''

        self.cursor_home (self.cur_r, 1)

    def lf (self):
        '''This moves the cursor down with scrolling.
        '''

        old_r = self.cur_r
        self.cursor_down()
        if old_r == self.cur_r:
            self.scroll_up ()
            self.erase_line()

    def crlf (self):
        '''This advances the cursor with CRLF properties.
        The cursor will line wrap and the screen may scroll.
        '''

        self.cr ()
        self.lf ()

    def newline (self):
        '''This is an alias for crlf().
        '''

        self.crlf()

    def put_abs (self, r, c, ch):
        '''Screen array starts at 1 index.'''

        r = constrain (r, 1, self.rows)
        c = constrain (c, 1, self.cols)
        if isinstance(ch, bytes):
            ch = self._decode(ch)[0]
        else:
            ch = ch[0]
        self.w[r-1][c-1] = ch

    def put (self, ch):
        '''This puts a characters at the current cursor position.
        '''

        if isinstance(ch, bytes):
            ch = self._decode(ch)

        self.put_abs (self.cur_r, self.cur_c, ch)

    def insert_abs (self, r, c, ch):
        '''This inserts a character at (r,c). Everything under
        and to the right is shifted right one character.
        The last character of the line is lost.
        '''

        if isinstance(ch, bytes):
            ch = self._decode(ch)

        r = constrain (r, 1, self.rows)
        c = constrain (c, 1, self.cols)
        for ci in range (self.cols, c, -1):
            self.put_abs (r,ci, self.get_abs(r,ci-1))
        self.put_abs (r,c,ch)

    def insert (self, ch):

        if isinstance(ch, bytes):
            ch = self._decode(ch)

        self.insert_abs (self.cur_r, self.cur_c, ch)

    def get_abs (self, r, c):

        r = constrain (r, 1, self.rows)
        c = constrain (c, 1, self.cols)
        return self.w[r-1][c-1]

    def get (self):

        self.get_abs (self.cur_r, self.cur_c)

    def get_region (self, rs,cs, re,ce):
        '''This returns a list of lines representing the region.
        '''

        rs = constrain (rs, 1, self.rows)
        re = constrain (re, 1, self.rows)
        cs = constrain (cs, 1, self.cols)
        ce = constrain (ce, 1, self.cols)
        if rs > re:
            rs, re = re, rs
        if cs > ce:
            cs, ce = ce, cs
        sc = []
        for r in range (rs, re+1):
            line = u''
            for c in range (cs, ce + 1):
                ch = self.get_abs (r,c)
                line = line + ch
            sc.append (line)
        return sc

    def cursor_constrain (self):
        '''This keeps the cursor within the screen area.
        '''

        self.cur_r = constrain (self.cur_r, 1, self.rows)
        self.cur_c = constrain (self.cur_c, 1, self.cols)

    def cursor_home (self, r=1, c=1): # <ESC>[{ROW};{COLUMN}H

        self.cur_r = r
        self.cur_c = c
        self.cursor_constrain ()

    def cursor_back (self,count=1): # <ESC>[{COUNT}D (not confused with down)

        self.cur_c = self.cur_c - count
        self.cursor_constrain ()

    def cursor_down (self,count=1): # <ESC>[{COUNT}B (not confused with back)

        self.cur_r = self.cur_r + count
        self.cursor_constrain ()

    def cursor_forward (self,count=1): # <ESC>[{COUNT}C

        self.cur_c = self.cur_c + count
        self.cursor_constrain ()

    def cursor_up (self,count=1): # <ESC>[{COUNT}A

        self.cur_r = self.cur_r - count
        self.cursor_constrain ()

    def cursor_up_reverse (self): # <ESC> M   (called RI -- Reverse Index)

        old_r = self.cur_r
        self.cursor_up()
        if old_r == self.cur_r:
            self.scroll_up()

    def cursor_force_position (self, r, c): # <ESC>[{ROW};{COLUMN}f
        '''Identical to Cursor Home.'''

        self.cursor_home (r, c)

    def cursor_save (self): # <ESC>[s
        '''Save current cursor position.'''

        self.cursor_save_attrs()

    def cursor_unsave (self): # <ESC>[u
        '''Restores cursor position after a Save Cursor.'''

        self.cursor_restore_attrs()

    def cursor_save_attrs (self): # <ESC>7
        '''Save current cursor position.'''

        self.cur_saved_r = self.cur_r
        self.cur_saved_c = self.cur_c

    def cursor_restore_attrs (self): # <ESC>8
        '''Restores cursor position after a Save Cursor.'''

        self.cursor_home (self.cur_saved_r, self.cur_saved_c)

    def scroll_constrain (self):
        '''This keeps the scroll region within the screen region.'''

        if self.scroll_row_start <= 0:
            self.scroll_row_start = 1
        if self.scroll_row_end > self.rows:
            self.scroll_row_end = self.rows

    def scroll_screen (self): # <ESC>[r
        '''Enable scrolling for entire display.'''

        self.scroll_row_start = 1
        self.scroll_row_end = self.rows

    def scroll_screen_rows (self, rs, re): # <ESC>[{start};{end}r
        '''Enable scrolling from row {start} to row {end}.'''

        self.scroll_row_start = rs
        self.scroll_row_end = re
        self.scroll_constrain()

    def scroll_down (self): # <ESC>D
        '''Scroll display down one line.'''

        # Screen is indexed from 1, but arrays are indexed from 0.
        s = self.scroll_row_start - 1
        e = self.scroll_row_end - 1
        self.w[s+1:e+1] = copy.deepcopy(self.w[s:e])

    def scroll_up (self): # <ESC>M
        '''Scroll display up one line.'''

        # Screen is indexed from 1, but arrays are indexed from 0.
        s = self.scroll_row_start - 1
        e = self.scroll_row_end - 1
        self.w[s:e] = copy.deepcopy(self.w[s+1:e+1])

    def erase_end_of_line (self): # <ESC>[0K -or- <ESC>[K
        '''Erases from the current cursor position to the end of the current
        line.'''

        self.fill_region (self.cur_r, self.cur_c, self.cur_r, self.cols)

    def erase_start_of_line (self): # <ESC>[1K
        '''Erases from the current cursor position to the start of the current
        line.'''

        self.fill_region (self.cur_r, 1, self.cur_r, self.cur_c)

    def erase_line (self): # <ESC>[2K
        '''Erases the entire current line.'''

        self.fill_region (self.cur_r, 1, self.cur_r, self.cols)

    def erase_down (self): # <ESC>[0J -or- <ESC>[J
        '''Erases the screen from the current line down to the bottom of the
        screen.'''

        self.erase_end_of_line ()
        self.fill_region (self.cur_r + 1, 1, self.rows, self.cols)

    def erase_up (self): # <ESC>[1J
        '''Erases the screen from the current line up to the top of the
        screen.'''

        self.erase_start_of_line ()
        self.fill_region (self.cur_r-1, 1, 1, self.cols)

    def erase_screen (self): # <ESC>[2J
        '''Erases the screen with the background color.'''

        self.fill ()

    def set_tab (self): # <ESC>H
        '''Sets a tab at the current position.'''

        pass

    def clear_tab (self): # <ESC>[g
        '''Clears tab at the current position.'''

        pass

    def clear_all_tabs (self): # <ESC>[3g
        '''Clears all tabs.'''

        pass

#        Insert line             Esc [ Pn L
#        Delete line             Esc [ Pn M
#        Delete character        Esc [ Pn P
#        Scrolling region        Esc [ Pn(top);Pn(bot) r

