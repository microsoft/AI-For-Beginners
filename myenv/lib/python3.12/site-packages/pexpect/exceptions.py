"""Exception classes used by Pexpect"""

import traceback
import sys

class ExceptionPexpect(Exception):
    '''Base class for all exceptions raised by this module.
    '''

    def __init__(self, value):
        super(ExceptionPexpect, self).__init__(value)
        self.value = value

    def __str__(self):
        return str(self.value)

    def get_trace(self):
        '''This returns an abbreviated stack trace with lines that only concern
        the caller. In other words, the stack trace inside the Pexpect module
        is not included. '''

        tblist = traceback.extract_tb(sys.exc_info()[2])
        tblist = [item for item in tblist if ('pexpect/__init__' not in item[0])
                                           and ('pexpect/expect' not in item[0])]
        tblist = traceback.format_list(tblist)
        return ''.join(tblist)


class EOF(ExceptionPexpect):
    '''Raised when EOF is read from a child.
    This usually means the child has exited.'''


class TIMEOUT(ExceptionPexpect):
    '''Raised when a read time exceeds the timeout. '''
