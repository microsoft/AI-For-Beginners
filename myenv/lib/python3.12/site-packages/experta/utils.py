from functools import singledispatch
import collections.abc

from frozendict import frozendict

from .fieldconstraint import P


class frozenlist(tuple):
    def __repr__(self):
        return "frozenlist([%s])" % (super().__repr__()[1:-1], )


@singledispatch
def freeze(obj):
    if isinstance(obj, collections.abc.Hashable):
        return obj
    else:
        raise TypeError(
            ("type(%r) => %s is not hashable, "
             "see `experta.utils.freeze` docs to register your "
             "own freeze method") % (obj, type(obj)))


@freeze.register(dict)
@freeze.register(frozendict)
def freeze_dict(obj):
    return frozendict((k, freeze(v)) for k, v in obj.items())


@freeze.register(list)
@freeze.register(frozenlist)
def freeze_list(obj):
    return frozenlist(freeze(v) for v in obj)


@freeze.register(set)
@freeze.register(frozenset)
def freeze_set(obj):
    return frozenset(freeze(v) for v in obj)


@singledispatch
def unfreeze(obj):
    return obj


@unfreeze.register(dict)
@unfreeze.register(frozendict)
def unfreeze_frozendict(obj):
    return {k: unfreeze(v) for k, v in obj.items()}


@unfreeze.register(list)
@unfreeze.register(frozenlist)
def unfreeze_frozenlist(obj):
    return [unfreeze(x) for x in obj]


@unfreeze.register(set)
@unfreeze.register(frozenset)
def unfreeze_frozenset(obj):
    return {unfreeze(x) for x in obj}


def anyof(*what):
    return P(lambda y: y in what)
