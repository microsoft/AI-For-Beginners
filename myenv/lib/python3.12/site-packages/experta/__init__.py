__version__ = '1.9.4'

try:
    from .conditionalelement import AND, OR, NOT, TEST, EXISTS, FORALL
    from .engine import KnowledgeEngine
    from .fact import Fact, InitialFact, Field
    from .fieldconstraint import L, W, P
    from .rule import Rule
    from .watchers import watch, unwatch
    from .deffacts import DefFacts
    from .shortcuts import MATCH, AS
    from .operator import *
except ImportError:
    pass
