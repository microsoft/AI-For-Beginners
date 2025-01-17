class Bindable:
    def __rlshift__(self, other):
        if not isinstance(other, str):
            raise TypeError("%s can only be binded to a string" % self)
        elif self.__bind__ is not None:
            raise RuntimeError("%s can only be binded once" % repr(self))
        else:
            self.__bind__ = other
            return self

    def __hash__(self):
        return hash((self.__bind__, ) + tuple(self))

    def __eq__(self, other):
        return (self.__class__ == other.__class__
                and self.__bind__ == other.__bind__
                and super().__eq__(other))
