"""
RETE nodes implementation.

This are the node types needed by this RETE implementation. Some node
types (like `The One-input Node for Testing Variable Bindings) are not
needed in this implementation.

"""
from collections.abc import Mapping
from contextlib import suppress
from itertools import chain

from experta.activation import Activation
from experta.rule import Rule
from experta.watchers import MATCHER, MATCH

from . import mixins
from .abstract import Node, OneInputNode, TwoInputNode
from .token import Token


class BusNode(mixins.AnyChild,
              mixins.NoMemory,
              Node):
    """
    The Bus Node.

    The node that reports working memory changes to the rest of the
    network.

    This node cannot be activated in the same manner as the other nodes.
    No tokens can be sent to it since this is the node where the first
    tokens are built.
    """

    def add(self, fact):
        """Create a VALID token and send it to all children."""
        token = Token.valid(fact)
        MATCHER.debug("<BusNode> added %r", token)
        for child in self.children:
            child.callback(token)

    def remove(self, fact):
        """Create an INVALID token and send it to all children."""
        token = Token.invalid(fact)
        MATCHER.debug("<BusNode> added %r", token)
        for child in self.children:
            child.callback(token)


class WhereNode(mixins.AnyChild,
                mixins.HasMatcher,
                mixins.NoMemory,
                OneInputNode):
    """
    Check some conditions over a token context.

    """
    def _activate(self, token):
        if self.matcher(token.context):
            for child in self.children:
                child.callback(token)


class FeatureTesterNode(mixins.AnyChild,
                        mixins.HasMatcher,
                        mixins.NoMemory,
                        OneInputNode):
    """
    Feature Tester Node.

    This node implementation represents two different nodes in the
    original paper: `The One-input Node for Testing Constant Features`
    and `The One-input Node for Testing Variable Bindings`.

    The trick here is this node receives a callable object at
    initilization time and uses it for testing the received tokens on
    activation. The given callable can return one of the following
    things:

      - Boolean:

        - `True`: The test pass. The token will be sent to the children
          nodes.

        - `False`: The test failed. Do nothing.

      - Mapping (dict):

        - With content: The test pass. In addition the pairs key-value
          will be added to the token context.

        - Empty: The test failed. Do nothing.

    The only exception here is when the callable returns a mapping with
    some key and some value, and the current context of the token also
    have an entry for this key but with a different value. In this case
    the test do not pass.
    """

    def _activate(self, token):
        """
        Activate this node.

        Test the given token with this token matcher function and iff
        the test pass update the token and pass to all children.

        """
        try:
            assert len(token.data) == 1
        except AssertionError as exc:
            raise ValueError(exc) from exc
        else:
            fact = list(token.data)[0]

        match = self.matcher(fact)

        if match:
            if isinstance(match, Mapping):
                for key, value in match.items():
                    if isinstance(key, tuple):  # Negated condition
                        if key[1] in token.context \
                                and token.context[key[1]] == value:
                            return False
                    else:
                        if token.context.get(key, value) != value:
                            return False
                        if (False, key) in token.context \
                                and token.context[(False, key)] == value:
                            return False
                token.context.update(match)
            for child in self.children:
                child.callback(token)


class OrdinaryMatchNode(mixins.AnyChild,
                        mixins.HasMatcher,
                        TwoInputNode):
    """
    Ordinary Two-input Node.

    This kind of node receive tokens at two ports (left and right) and
    try to match them.

    The matching function is a callable given as a parameter to __init__
    and stored internally. This functions will receive two contexts, one
    from the left and other from the right, and decides if they match
    together (returning True or False).

    Matching pairs will be combined in one token containing facts from
    both and a combined context. This combined tokens will be sent to
    all children.
    """

    def _reset(self):
        """Wipe node memory."""
        self.left_memory = list()
        self.right_memory = list()

    def __activation(self, token, branch_memory, matching_memory,
                     is_left=True):
        """
        Node activation internal function.

        This is a generalization of both activation functions.

        The given token is added or removed from `branch_memory`
        depending of its tag.

        For any other data in `matching_memory` the match function will
        be called and if a match occurs a new token will be produced and
        sent to all children.

        """
        if token.is_valid():
            branch_memory.append(token.to_info())
        else:
            with suppress(ValueError):
                branch_memory.remove(token.to_info())

        for other_data, other_context in matching_memory:
            other_context = dict(other_context)
            if is_left:
                left_context = token.context
                right_context = other_context
            else:
                left_context = other_context
                right_context = token.context

            match = self.matcher(left_context, right_context)

            if match:
                MATCH.info("%s (%s | %s) = True",
                           self.__class__.__name__,
                           left_context,
                           right_context)

                newcontext = {k: v for k, v in token.context.items()
                              if isinstance(k, str)}

                for k, v in other_context.items():
                    if not isinstance(k, tuple):
                        # Negated value are not needed any further
                        newcontext[k] = v

                newtoken = Token(token.tag,
                                 token.data | other_data,
                                 newcontext)

                for child in self.children:
                    child.callback(newtoken)
            else:
                MATCH.debug("%s (%s | %s) = False",
                            self.__class__.__name__,
                            left_context,
                            right_context)

    def _activate_left(self, token):
        """Node left activation."""
        self.__activation(token,
                          self.left_memory,
                          self.right_memory,
                          is_left=True)

    def _activate_right(self, token):
        """Node right activation."""
        self.__activation(token,
                          self.right_memory,
                          self.left_memory,
                          is_left=False)


class ConflictSetNode(mixins.AnyChild,
                      OneInputNode):
    """
    Conflict Set Change Node.

    This node is the final step in the network. Any token activating
    this node will produce an activation (VALID token) or deactivation
    (INVALID token) of the internal `rule` with the token context and
    facts.
    """

    def __init__(self, rule):
        """Initialize the node with the given `rule`."""
        try:
            assert isinstance(rule, Rule)
        except AssertionError as exc:
            raise TypeError(exc) from exc
        else:
            self.rule = rule

        self.added = set()
        self.removed = set()

        super().__init__()

    def _reset(self):
        """Wipe the node internal memory."""
        self.memory = set()

    def _activate(self, token):
        """Activate this node for the given token."""

        info = token.to_info()

        activation = Activation(
            self.rule,
            frozenset(info.data),
            {k: v for k, v in info.context if isinstance(k, str)})

        if token.is_valid():
            if info not in self.memory:
                self.memory.add(info)
                if activation in self.removed:
                    self.removed.remove(activation)
                else:
                    self.added.add(activation)
        else:
            try:
                self.memory.remove(info)
            except ValueError:
                pass
            else:
                if activation in self.added:
                    self.added.remove(activation)
                else:
                    self.removed.add(activation)

    def get_activations(self):
        """Return a list of activations."""
        res = (self.added, self.removed)

        self.added = set()
        self.removed = set()

        return res

    def __str__(self):  # pragma: no cover
        return "%s: %s" % (self.__class__.__name__, self.rule.__name__)


class NotNode(mixins.AnyChild,
              mixins.HasMatcher,
              TwoInputNode):
    """
    Not Node.

    This is a special kind of node representing the absence of some
    fact/condition.

    This node is similar to `OrdinaryMatchNode` in the sense it has two
    input ports and try to match tokens arriving in both of them. But
    pass VALID tokens to the children when no matches are found and
    INVALID tokens when they are.
    """

    def _reset(self):
        """Wipe node internal memory."""
        self.left_memory = dict()
        self.right_memory = list()

    def _activate_left(self, token):
        """
        Activate from the left.

        In case of a valid token this activations test the right memory
        with the given token and looks for the number of matches. The
        token and the number of occurences are stored in the left
        memory.

        If the number of matches is zero the token activates all children.

        """
        if not self.right_memory:
            if token.is_valid():
                self.left_memory[token.to_info()] = 0
            else:
                del self.left_memory[token.to_info()]

            for child in self.children:
                child.callback(token)

        elif token.is_valid():
            count = 0

            for _, right_context in self.right_memory:
                if self.matcher(token.context, dict(right_context)):
                    count += 1

            if count == 0:
                for child in self.children:
                    child.callback(token)

            self.left_memory[token.to_info()] = count
        else:
            count = 0
            for _, right_context in self.right_memory:
                if self.matcher(token.context, dict(right_context)):
                    count += 1
                    break

            if count == 0:
                for child in self.children:
                    child.callback(token)

            del self.left_memory[token.to_info()]

    def _activate_right(self, token):
        """
        Activate from the right.

        Go over the left memory and find matching data, when found
        update the counter (substracting if the given token is invalid
        and adding otherwise). Depending on the result of this operation
        a new token is generated and passing to all children.

        """
        if token.is_valid():
            self.right_memory.append(token.to_info())
            inc = 1
        else:
            inc = -1
            self.right_memory.remove(token.to_info())

        for left in self.left_memory:
            if self.matcher(dict(left.context), token.context):
                self.left_memory[left] += inc
                newcount = self.left_memory[left]
                if (newcount == 0 and inc == -1) or \
                        (newcount == 1 and inc == 1):
                    if inc == -1:
                        newtoken = left.to_valid_token()
                    else:
                        newtoken = left.to_invalid_token()

                    for child in self.children:
                        child.callback(newtoken)
