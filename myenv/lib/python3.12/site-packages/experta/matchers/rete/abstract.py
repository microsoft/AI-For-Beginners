"""Abstract base classes for the RETE implementation."""
import abc

from experta import watchers


class Node(metaclass=abc.ABCMeta):
    """Node interface."""

    def __init__(self):
        """Initialize `self.children` and reset the node own memory."""
        self.children = list()
        self._reset()  # Reset it's OWN memory.

    @abc.abstractmethod
    def add_child(self, child, callback):  # pragma: no cover
        """Add a child to `self.children` if necessary."""
        pass

    def reset(self):
        """Reset itself and recursively all its children."""
        watchers.MATCHER.debug("Node <%s> reset", self)
        self._reset()
        for child in self.children:
            child.node.reset()

    @abc.abstractmethod
    def _reset(self):  # pragma: no cover
        """Reset this node's memory."""
        pass

    def __str__(self):  # pragma: no cover
        return self.__class__.__name__


class OneInputNode(Node):
    """Nodes which only have one input port."""

    def activate(self, token):
        """Make a copy of the received token and call `self._activate`."""

        if watchers.worth('MATCHER', 'DEBUG'):  # pragma: no cover
            watchers.MATCHER.debug(
                "Node <%s> activated with token %r", self, token)

        return self._activate(token.copy())

    @abc.abstractproperty
    def _activate(self, token):  # pragma: no cover
        """Node activation routine."""
        pass


class TwoInputNode(Node):
    """Nodes which have two input ports: left and right."""

    def activate_left(self, token):
        """Make a copy of the received token and call `_activate_left`."""
        watchers.MATCHER.debug(
            "Node <%s> activated left with token %r", self, token)
        return self._activate_left(token.copy())

    @abc.abstractproperty
    def _activate_left(self, token):  # pragma: no cover
        """Node left activation routine."""
        pass

    def activate_right(self, token):
        """Make a copy of the received token and call `_activate_right`."""
        watchers.MATCHER.debug(
            "Node <%s> activated right with token %r", self, token)
        return self._activate_right(token.copy())

    @abc.abstractproperty
    def _activate_right(self, token):  # pragma: no cover
        """Node right activation routine."""
        pass

    def __str__(self):  # pragma: no cover
        return self.__class__.__name__


class Check(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, fact):  # pragma: no cover
        """
        Given a `Fact` or a subclass of `Fact`, return:

            * `True` if the check matched.
            * `False` if the check didn't match.
            * A non empty `Mapping` meaning the check matched and yield
              some context.

        """
        pass

    def __str__(self):  # pragma: no cover
        return self.__class__.__name__
