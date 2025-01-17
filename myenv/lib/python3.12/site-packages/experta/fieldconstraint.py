from collections.abc import Callable

from experta.conditionalelement import ConditionalElement
from experta.pattern import Bindable

__all__ = ['L', 'W', 'P']


class FieldConstraint(ConditionalElement):
    def __and__(self, other):
        if isinstance(self, ANDFC) and isinstance(other, ANDFC):
            return ANDFC(*[x for x in chain(self, other)])
        elif isinstance(self, ANDFC):
            return ANDFC(*[x for x in self]+[other])
        elif isinstance(other, ANDFC):
            return ANDFC(*[self]+[x for x in other])
        else:
            return ANDFC(self, other)

    def __or__(self, other):
        if isinstance(self, ORFC) and isinstance(other, ORFC):
            return ORFC(*[x for x in chain(self, other)])
        elif isinstance(self, ORFC):
            return ORFC(*[x for x in self]+[other])
        elif isinstance(other, ORFC):
            return ORFC(*[self]+[x for x in other])
        else:
            return ORFC(self, other)

    def __invert__(self):
        return NOTFC(self)


class ANDFC(FieldConstraint):
    pass


class ORFC(FieldConstraint):
    pass


class NOTFC(FieldConstraint):
    def __rlshift__(self, other):
        """Pass the binding to the internal element."""
        self[0].__rlshift__(other)
        return self


class L(Bindable, FieldConstraint):
    """Literal Field Constraint"""
    def __new__(cls, value, __bind__=None):
        obj = super(L, cls).__new__(cls, value)
        obj.__bind__ = __bind__
        return obj

    @property
    def value(self):
        return self[0]

    def __repr__(self):  # pragma: no cover
        return "L(%r)" % self.value


class W(Bindable, FieldConstraint):
    """Wildcard Field Constraint"""
    def __new__(cls, __bind__=None):
        obj = super(W, cls).__new__(cls)
        obj.__bind__ = __bind__
        return obj

    def __repr__(self):  # pragma: no cover
        return "W()" if self.__bind__ is None else "W(%r)" % self.__bind__


class P(Bindable, FieldConstraint):
    """Predicate Field Constraint"""
    def __new__(cls, match, __bind__=None):
        if not isinstance(match, Callable):
            raise TypeError("PredicateFC needs a callable.")
        else:
            obj = super(P, cls).__new__(cls, match)
            obj.__bind__ = __bind__
            return obj

    @property
    def match(self):
        return self[0]
