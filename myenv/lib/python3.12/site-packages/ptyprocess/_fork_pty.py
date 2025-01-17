"""Substitute for the forkpty system call, to support Solaris.
"""
import os
import errno

from pty import (STDIN_FILENO, STDOUT_FILENO, STDERR_FILENO, CHILD)
from .util import PtyProcessError

def fork_pty():
    '''This implements a substitute for the forkpty system call. This
    should be more portable than the pty.fork() function. Specifically,
    this should work on Solaris.

    Modified 10.06.05 by Geoff Marshall: Implemented __fork_pty() method to
    resolve the issue with Python's pty.fork() not supporting Solaris,
    particularly ssh. Based on patch to posixmodule.c authored by Noah
    Spurrier::

        http://mail.python.org/pipermail/python-dev/2003-May/035281.html

    '''

    parent_fd, child_fd = os.openpty()
    if parent_fd < 0 or child_fd < 0:
        raise OSError("os.openpty() failed")

    pid = os.fork()
    if pid == CHILD:
        # Child.
        os.close(parent_fd)
        pty_make_controlling_tty(child_fd)

        os.dup2(child_fd, STDIN_FILENO)
        os.dup2(child_fd, STDOUT_FILENO)
        os.dup2(child_fd, STDERR_FILENO)

    else:
        # Parent.
        os.close(child_fd)

    return pid, parent_fd

def pty_make_controlling_tty(tty_fd):
    '''This makes the pseudo-terminal the controlling tty. This should be
    more portable than the pty.fork() function. Specifically, this should
    work on Solaris. '''

    child_name = os.ttyname(tty_fd)

    # Disconnect from controlling tty, if any.  Raises OSError of ENXIO
    # if there was no controlling tty to begin with, such as when
    # executed by a cron(1) job.
    try:
        fd = os.open("/dev/tty", os.O_RDWR | os.O_NOCTTY)
        os.close(fd)
    except OSError as err:
        if err.errno != errno.ENXIO:
            raise

    os.setsid()

    # Verify we are disconnected from controlling tty by attempting to open
    # it again.  We expect that OSError of ENXIO should always be raised.
    try:
        fd = os.open("/dev/tty", os.O_RDWR | os.O_NOCTTY)
        os.close(fd)
        raise PtyProcessError("OSError of errno.ENXIO should be raised.")
    except OSError as err:
        if err.errno != errno.ENXIO:
            raise

    # Verify we can open child pty.
    fd = os.open(child_name, os.O_RDWR)
    os.close(fd)

    # Verify we now have a controlling tty.
    fd = os.open("/dev/tty", os.O_WRONLY)
    os.close(fd)
