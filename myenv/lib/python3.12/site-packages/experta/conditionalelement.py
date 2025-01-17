__all__ = ['AND', 'OR', 'NOT', 'TEST', 'EXISTS', 'FORALL']


class ConditionalElement(tuple):
    """Base Conditional Element"""

    def __new__(cls, *args):
        return super(ConditionalElement, cls).__new__(cls, args)

    def __repr__(self):  # pragma: no cover
        return "%s%s" % (self.__class__.__name__, super().__repr__())


class OperableCE:
    def __and__(self, other):
        if isinstance(self, AND) and isinstance(other, AND):
            return AND(*[x for x in chain(self, other)])
        elif isinstance(self, AND):
            return AND(*[x for x in self]+[other])
        elif isinstance(other, AND):
            return AND(*[self]+[x for x in other])
        else:
            return AND(self, other)

    def __or__(self, other):
        if isinstance(self, OR) and isinstance(other, OR):
            return OR(*[x for x in chain(self, other)])
        elif isinstance(self, OR):
            return OR(*[x for x in self]+[other])
        elif isinstance(other, OR):
            return OR(*[self]+[x for x in other])
        else:
            return OR(self, other)

    def __invert__(self):
        return NOT(self)


class AND(OperableCE, ConditionalElement):
    pass


class OR(OperableCE, ConditionalElement):
    pass


class NOT(OperableCE, ConditionalElement):
    pass


class TEST(OperableCE, ConditionalElement):
    pass


class EXISTS(OperableCE, ConditionalElement):
    pass


class FORALL(OperableCE, ConditionalElement):
    pass
