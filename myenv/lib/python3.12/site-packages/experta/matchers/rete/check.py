from collections import namedtuple
from collections.abc import Mapping
from functools import singledispatch
import dis
import inspect

from experta.fieldconstraint import FieldConstraint
from experta.fieldconstraint import L, P, W
from experta.fieldconstraint import ANDFC, ORFC, NOTFC
from .abstract import Check
from experta.watchers import MATCH


CheckFunction = namedtuple('CheckFunction',
                           ['key_a', 'key_b', 'expected', 'check'])


class TypeCheck(Check, namedtuple('_TypeCheck', ['fact_type'])):

    _instances = dict()

    def __new__(cls, fact_type):
        if fact_type not in cls._instances:
            cls._instances[fact_type] = super().__new__(cls, fact_type)
        return cls._instances[fact_type]

    def __call__(self, fact):
        res = type(fact) == self.fact_type

        log = MATCH.info if res else MATCH.debug
        log("type(%s) == %s = %r",
            fact, self.fact_type.__name__, res)

        return res

    def __str__(self):  # pragma: no cover
        return "type() == %s" % self.fact_type.__name__


class FactCapture(Check, namedtuple('_FactCapture', ['bind'])):

    _instances = dict()

    def __new__(cls, bind):
        if bind not in cls._instances:
            cls._instances[bind] = super().__new__(cls, bind)
        return cls._instances[bind]

    @property
    def __bind__(self):
        return self.bind

    def __call__(self, fact):
        MATCH.info("%r <= %s", self.__bind__, fact)
        return {self.__bind__: fact}

    def __str__(self):  # pragma: no cover
        return "%s <= <Fact>" % (self.__bind__)


class FeatureCheck(Check,
                   namedtuple('_FeatureCheck',
                              ['what', 'how', 'check', 'expected'])):

    _instances = dict()

    def __new__(cls, what, how):
        if not isinstance(how, FieldConstraint):
            how = L(how)

        check_function = cls.get_check_function(how, what)

        key = (what, check_function.key_a, check_function.key_b)

        if key not in cls._instances:
            cls._instances[key] = super(Check, cls).__new__(
                cls,
                what,
                how,
                check_function.check,
                check_function.expected)

        return cls._instances[key]

    def __call__(self, data, is_fact=True):
        if is_fact:
            if isinstance(self.what, str):
                record = data
                if (not self.what.startswith('__')
                        and not self.what.endswith('__')):
                    try:
                        for p in self.what.split('__'):
                            if p.isnumeric():
                                p = int(p)
                            record = record[p]
                    except (IndexError, KeyError, TypeError):
                        return False
            else:
                try:
                    record = data[self.what]
                except (IndexError, KeyError, TypeError):
                    return False
        else:
            record = data

        res = self.check(record, self.expected)

        log = MATCH.info if res else MATCH.debug
        log("what=%r, how=%r, fact=%s = %r", self.what, self.how, data, res)

        return res

    def __str__(self):  # pragma: no cover
        return "%s (%s) %s" % (self.what, self.check.__name__, self.expected)

    @singledispatch
    @staticmethod
    def get_check_function(pce, what=None):
        raise TypeError("Unknown FieldConstraint type.")

    @get_check_function.register(L)
    def _(pce, what=None):
        def equal_literal(actual, expected):
            if expected.value == actual:
                if expected.__bind__ is None:
                    return True
                else:
                    return {expected.__bind__: actual}
            else:
                return False

        return CheckFunction(key_a=L,
                             key_b=(pce.value, pce.__bind__),
                             expected=pce,
                             check=equal_literal)

    @get_check_function.register(P)
    def _(pce, what=None):
        def match_predicate(actual, expected):
            if expected.match(actual):
                if expected.__bind__ is None:
                    return True
                else:
                    return {expected.__bind__: actual}
            else:
                return False

        key_b = ('ID',
                 id(pce.match),
                 pce.__bind__)

        return CheckFunction(key_a=P,
                             key_b=key_b,
                             expected=pce,
                             check=match_predicate)

    @get_check_function.register(W)
    def _(pce, what=None):
        def wildcard_match(actual, expected):
            if expected.__bind__ is None:
                return True
            else:
                return {expected.__bind__: actual}

        return CheckFunction(key_a=W,
                             key_b=pce.__bind__,
                             expected=pce,
                             check=wildcard_match)

    @get_check_function.register(NOTFC)
    def _(pce, what=None):
        def not_equal(actual, expected):
            subresult = expected(actual, is_fact=False)
            if isinstance(subresult, Mapping):
                newresult = {(False, k): v
                             for k, v in subresult.items()}
                return newresult
            else:
                return not subresult

        key_b = FeatureCheck(what, pce[0])

        return CheckFunction(key_a=NOTFC,
                             key_b=key_b,
                             expected=key_b,
                             check=not_equal)

    @get_check_function.register(ANDFC)
    def _(pce, what=None):
        def and_match(actual, expected):
            value = dict()
            for subcheck in expected:
                subres = subcheck(actual, is_fact=False)
                if subres is False:
                    break
                elif subres is True:
                    pass
                elif isinstance(subres, Mapping):
                    value.update(subres)
                else:
                    raise TypeError('Bad check value.')
            else:
                if not value:
                    return True
                else:
                    return value
            return False

        key_b = tuple(FeatureCheck(what, x) for x in pce)

        return CheckFunction(key_a=ANDFC,
                             key_b=key_b,
                             expected=key_b,
                             check=and_match)

    @get_check_function.register(ORFC)
    def _(pce, what=None):
        def or_match(actual, expected):
            for subcheck in expected:
                subres = subcheck(actual, is_fact=False)
                if subres:
                    return subres
            else:
                return False

        key_b = tuple(FeatureCheck(what, x) for x in pce)

        return CheckFunction(key_a=ORFC,
                             key_b=key_b,
                             expected=key_b,
                             check=or_match)


class SameContextCheck(Check):
    def __call__(self, l, r):
        for key, value in l.items():
            if key[0] is False:
                raise RuntimeError(
                    'Negated value "%s" present before capture.' % key[1])
            else:
                if key in r and value != r[key]:
                    return False
                if (False, key) in r and value == r[(False, key)]:
                    return False
        else:
            return True


class WhereCheck(Check, namedtuple('_WhereCheck', ['test'])):

    _instances = dict()

    def __new__(cls, test):
        if test not in cls._instances:
            obj = super().__new__(cls, test)
            obj.parameters = inspect.signature(test).parameters.keys()
            cls._instances[test] = obj

        return cls._instances[test]

    def __call__(self, context):
        parameters = {k: context.get(k) for k in self.parameters}
        res = self.test(**parameters)

        log = MATCH.info if res else MATCH.debug
        log("TEST %r(%r) == %r", self.test, parameters, res)

        return res
