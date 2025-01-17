"""
The operator module contains a set of predicate functions constructors based on
the P() field constraint.

These operators can be composed together and binded like normal Field
Constraints.

Example:

>>> WIDTH = 640
>>> HEIGHT = 480
>>>
>>> class Player(Fact):
...      pass
...
>>>
>>> @Rule(
...      Player(
...          x=MATCH.x & GE(0) & LE(WIDTH),
...          y=MATCH.y & BETWEEN(0, HEIGHT),
...          name=MATCH.name & (CALL.startswith("@") | CALL.endswith("_ADM"))
...      )
... )
... def admin_in_visible_area(self, x, y, name):
...     pass
...

"""
from itertools import chain
import operator as op
import re
import fnmatch

from .conditionalelement import ConditionalElement
from .fieldconstraint import P

__all__ = ['TRUTH', 'LT', 'LE', 'EQ', 'NE', 'GE', 'GT', 'IS', 'IS_NOT',
           'CONTAINS', 'BETWEEN', 'CALL', 'REGEX', 'LIKE', 'ILIKE']


def _from_operator2(o):
    def __from_operator2(b):
        if isinstance(b, ConditionalElement):
            raise TypeError(
                "A ConditionalElement can't be used as an operator condition.")
        else:
            return P(lambda a: o(a, b))
    return __from_operator2


#: Return True if obj is true, and False otherwise. This is equivalent to using
#: the bool constructor.
TRUTH = P(bool)

#: Less than operator.
LT = _from_operator2(op.lt)

#: Less than or equal operator.
LE = _from_operator2(op.le)

#: Equal operator.
EQ = _from_operator2(op.eq)

#: Not equal operator.
NE = _from_operator2(op.ne)

#: Greater than or equal operator.
GE = _from_operator2(op.ge)

#: Greater than operator.
GT = _from_operator2(op.gt)

#: Tests object identity.
IS = _from_operator2(op.is_)

#: Tests object identity.
IS_NOT = _from_operator2(op.is_not)

#: Return the outcome of the test b in a
CONTAINS = _from_operator2(op.contains)


def BETWEEN(a, b):
    """
    The BETWEEN operator selects values within a given range.
    The BETWEEN operator is inclusive: begin and end values are included.

    """
    if any((isinstance(x, ConditionalElement) for x in (a, b))):
        raise TypeError(
            "A ConditionalElement can't be used as an operator condition.")
    else:
        return P(lambda x: a <= x <= b)


class _CALL:
    """
    Syntactic sugar for predicates which invoque functions who call a captured
    value method.

    >>> @Rule(Fact(quantity=P(lambda q: q.isnumeric()))
        def something(...):
            ...

    Is equivalent to:

    >>> @Rule(Fact(quantity=CALL.isnumeric()))
        def something(...):
            ...

    """
    def __getattr__(self, name):
        def _call(*args, **kwargs):
            if any((isinstance(x, ConditionalElement)
                    for x in chain(args, kwargs.values()))):
                raise TypeError(
                    ("A ConditionalElement can't be used as an "
                     "operator condition."))
            else:
                return P(lambda x: getattr(x, name)(*args, **kwargs))
        return _call


CALL = _CALL()


def REGEX(pattern, flags=0):
    """Regular expression matching."""
    return P(lambda x: re.match(pattern, x, flags=flags))


def LIKE(pattern):
    """Unix shell-style wildcards. Case-sensitive"""
    return P(lambda x: fnmatch.fnmatchcase(x, pattern))


def ILIKE(pattern):
    """Unix shell-style wildcards. Case-insensitive"""
    return P(lambda x: fnmatch.fnmatch(x.lower(), pattern.lower()))
