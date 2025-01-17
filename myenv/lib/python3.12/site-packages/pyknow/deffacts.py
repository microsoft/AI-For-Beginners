from functools import update_wrapper
import inspect


class DefFacts:
    def __new__(cls, nonexpected=None, order=0):
        obj = super(DefFacts, cls).__new__(cls)

        if nonexpected is not None:
            raise SyntaxError("DefFacts must be instanced to allow decoration")

        obj.__wrapped = None
        obj._wrapped_self = None
        obj.order = order

        return obj

    @property
    def _wrapped(self):
        return self.__wrapped

    @_wrapped.setter
    def _wrapped(self, value):
        if inspect.isgeneratorfunction(value):
            self.__wrapped = value
            return update_wrapper(self, self.__wrapped)
        else:
            raise TypeError("DefFact can only decorate generators.")

    def __repr__(self):  # pragma: no cover
        return "DefFacts(%r)" % (self._wrapped)

    def __call__(self, *args, **kwargs):
        if self._wrapped is not None:
            if self._wrapped_self is None:
                gen = self._wrapped(*args, **kwargs)
            else:
                gen = self._wrapped(self._wrapped_self, *args, **kwargs)
            return (x.copy() for x in gen)
        elif not args:
            raise RuntimeError("Usage error.")
        else:
            self._wrapped = args[0]
            return self

    def __get__(self, instance, owner):
        self._wrapped_self = instance
        return self
