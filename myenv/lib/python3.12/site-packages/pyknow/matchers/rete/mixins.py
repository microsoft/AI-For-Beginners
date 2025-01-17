"""Mixing classes for the RETE nodes."""
from collections import namedtuple
from collections.abc import Callable


#: Used to store node/callback pair in nodes children set.
ChildNode = namedtuple('ChildNode', ['node', 'callback'])


class NoMemory:
    """The node has no memory so we have nothing to do."""

    def _reset(self):
        pass


class AnyChild:
    """This node allow any kind of node as a child."""

    def add_child(self, node, callback):
        """Add node and callback to the children set."""
        if node not in self.children:
            self.children.append(ChildNode(node, callback))


class HasMatcher:
    """This node need a match callable as parameter."""

    def __init__(self, matcher):
        """If `matcher` is a callable, assign to `self.matcher`."""
        try:
            assert isinstance(matcher, Callable)
        except AssertionError as exc:
            raise TypeError(exc) from exc
        else:
            self.matcher = matcher

        super().__init__()

    def __str__(self):  # pragma: no cover
        return "%s: %s" % (self.__class__.__name__, self.matcher)
