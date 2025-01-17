"""Token object and related objects needed by the RETE algorithm."""

from collections import namedtuple
from collections.abc import Mapping
from enum import Enum

from experta.fact import Fact


class TokenInfo(namedtuple('_TokenInfo', ['data', 'context'])):
    """Tag agnostig version of Token with inmutable data."""

    def __new__(cls, data, context):
        """Return a namedtuple instance with inmutable data."""
        return super(TokenInfo, cls).__new__(cls,
                                             frozenset(data),
                                             frozenset(context.items()))

    def to_valid_token(self):
        """Create a VALID token using this data."""
        return Token.valid(self.data, dict(self.context))

    def to_invalid_token(self):
        """Create an INVALID token using this data."""
        return Token.invalid(self.data, dict(self.context))


class Token(namedtuple('_Token', ['tag', 'data', 'context'])):
    """Token, as described by RETE but with context."""

    class TagType(Enum):
        """Types of Token TAG data."""

        VALID = True
        INVALID = False

    def __new__(cls, tag, data, context=None):
        """
        Instantiate a new Token with the given tag, data and context.

        If the context is None an empty context will be generated.

        - `tag`: Must be an instance of `TagType`.
        - `data`: A Fact or an iterable of Facts.
        - `context`: A mapping or None.

        """
        if context is None:
            context = {}

        try:
            assert isinstance(tag, cls.TagType), \
                "tag must be of `Token.TagType` type"
            assert (isinstance(data, Fact) or
                    all(isinstance(f, Fact) for f in data)), \
                "data must be either Fact or iterable of Facts"
            assert isinstance(context, Mapping)
        except AssertionError as exc:
            raise TypeError(exc) from exc

        data = {data} if isinstance(data, Fact) else set(data)
        self = super(Token, cls).__new__(cls, tag, data, context)
        return self

    def to_info(self):
        """
        Create and return an instance of TokenInfo with this token.

        This is useful, for example, to use this token information as a
        dictionary key.

        """
        return TokenInfo(self.data, self.context)

    @classmethod
    def valid(cls, data, context=None):
        """Shortcut to create a VALID Token."""
        return cls(cls.TagType.VALID, data, context)

    @classmethod
    def invalid(cls, data, context=None):
        """Shortcut to create an INVALID Token."""
        return cls(cls.TagType.INVALID, data, context)

    def is_valid(self):
        """Test if this Token is VALID."""
        return self.tag == self.TagType.VALID

    def copy(self):
        """
        Make a new instance of this Token.

        This method makes a copy of the mutable part of the token before
        making the instance.

        """
        return self.__class__(self.tag, self.data.copy(), self.context.copy())
