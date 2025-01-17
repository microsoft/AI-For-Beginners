from functools import singledispatch

from .check import FeatureCheck, TypeCheck, FactCapture, SameContextCheck
from .check import WhereCheck
from .dnf import dnf
from .nodes import ConflictSetNode, NotNode, OrdinaryMatchNode
from .nodes import WhereNode
from experta.conditionalelement import NOT, OR, AND, TEST, EXISTS, FORALL
from experta.fact import InitialFact, Fact
from experta.rule import Rule


@singledispatch
def prepare_rule(exp):
    """
    Given a rule, build a new one suitable for RETE network generation.

    Meaning:

        #. Rule is in disjuntive normal form (DNF).

        #. If the `rule` is empty is filled with an `InitialFact`.

        #. If the `rule` starts with a `NOT`, an `InitialFact` is prepended.

        #. If any AND starts with a `NOT`, an `InitialFact` is prepended.

        #. If the `rule` is an OR condition, each NOT inside will be
        converted to AND(InitialFact(), NOT(...))

    """
    return exp


@prepare_rule.register(Rule)
def _(exp):
    dnf_rule = dnf(exp)
    prep_rule = dnf_rule.new_conditions(
        *[prepare_rule(e) for e in dnf_rule])
    if not prep_rule:
        return prep_rule.new_conditions(InitialFact())
    elif isinstance(prep_rule[0], NOT) or len(extract_facts(prep_rule)) == 0:
        return prep_rule.new_conditions(InitialFact(), *prep_rule)
    else:
        return dnf(prep_rule)


@prepare_rule.register(OR)
def _(exp):
    or_exp = []
    for e in exp:
        if isinstance(e, NOT):
            or_exp.append(AND(InitialFact(), e))
        elif isinstance(e, AND):
            or_exp.append(prepare_rule(e))
        else:
            or_exp.append(e)
    return OR(*or_exp)


@prepare_rule.register(AND)
def _(exp):
    if isinstance(exp[0], NOT):
        return AND(InitialFact(), *exp)
    else:
        return exp


def extract_facts(rule):
    """Given a rule, return a set containing all rule LHS facts."""
    def _extract_facts(ce):
        if isinstance(ce, Fact):
            yield ce
        elif isinstance(ce, TEST):
            pass
        else:
            for e in ce:
                yield from _extract_facts(e)

    return set(_extract_facts(rule))


def generate_checks(fact):
    """Given a fact, generate a list of Check objects for checking it."""

    yield TypeCheck(type(fact))

    fact_captured = False
    for key, value in fact.items():
        if (isinstance(key, str)
                and key.startswith('__')
                and key.endswith('__')):
            # Special fact feature
            if key == '__bind__':
                yield FactCapture(value)
                fact_captured = True
            else:  # pragma: no cover
                yield FeatureCheck(key, value)
        else:
            yield FeatureCheck(key, value)

    # Assign the matching fact to the context
    if not fact_captured:
        yield FactCapture("__pattern_%s__" % id(fact))


def wire_rule(rule, alpha_terminals, lhs=None):
    if lhs is None:
        lhs = rule

    @singledispatch
    def _wire_rule(elem):
        raise TypeError("Unknown type %s" % type(elem))

    @_wire_rule.register(TEST)
    def _(elem):
        return WhereNode(WhereCheck(elem[0]))

    @_wire_rule.register(FORALL)
    def _(elem):
        leader = elem[0]
        followers = elem[1:]

        initial_fact_node = _wire_rule(InitialFact())
        leader_node = _wire_rule(leader)
        followers_node = _wire_rule(AND(*followers))
        not_node_1 = NotNode(SameContextCheck())
        not_node_2 = NotNode(SameContextCheck())

        # NotNode1
        followers_node.add_child(not_node_1, not_node_1.activate_right)
        leader_node.add_child(not_node_1, not_node_1.activate_left)

        # NotNode2
        not_node_1.add_child(not_node_2, not_node_2.activate_right)
        initial_fact_node.add_child(not_node_2, not_node_2.activate_left)

        return not_node_2

    @_wire_rule.register(EXISTS)
    def _(elem):
        # Create new nodes
        condition_node = _wire_rule(elem[0])
        initial_fact_node = _wire_rule(InitialFact())
        not_node_1 = NotNode(SameContextCheck())
        not_node_2 = NotNode(SameContextCheck())

        # NotNode1
        condition_node.add_child(not_node_1, not_node_1.activate_right)
        initial_fact_node.add_child(not_node_1, not_node_1.activate_left)

        # NotNode2
        initial_fact_node.add_child(not_node_2, not_node_2.activate_left)
        not_node_1.add_child(not_node_2, not_node_2.activate_right)

        return not_node_2

    @_wire_rule.register(Rule)
    @_wire_rule.register(AND)
    def _(elem):
        if len(elem) == 1:
            if isinstance(elem[0], Fact):
                return alpha_terminals[elem[0]]
            else:
                return _wire_rule(elem[0])
        else:  # > 1. Because < 1 is not possible at this point.
            current_node = None
            for f, s in zip(elem, elem[1:]):
                if isinstance(s, TEST):
                    if current_node is None:
                        current_node = _wire_rule(f)

                    # A TestNode after the previous node
                    new_node = _wire_rule(s)
                    current_node.add_child(new_node, new_node.activate)
                    current_node = new_node
                else:
                    if isinstance(s, NOT):
                        node_cls = NotNode
                    else:
                        node_cls = OrdinaryMatchNode

                    if current_node is None:
                        current_node = node_cls(SameContextCheck())
                        left_branch = _wire_rule(f)
                        right_branch = _wire_rule(s)
                    else:
                        left_branch = current_node
                        right_branch = _wire_rule(s)
                        current_node = node_cls(SameContextCheck())

                    left_branch.add_child(current_node,
                                          current_node.activate_left)
                    right_branch.add_child(current_node,
                                           current_node.activate_right)
            return current_node

    @_wire_rule.register(OR)
    def _(elem):
        raise SyntaxError(
            "You can't use an OR clause inside FORALL or EXISTS")

    @_wire_rule.register(Fact)
    def _(elem):
        return alpha_terminals[elem]

    @_wire_rule.register(NOT)
    def _(elem):
        return alpha_terminals[elem[0]]

    # Build beta network
    last_node = _wire_rule(lhs)

    # Add a new child to the last node to trigger the rule
    conflict_set_node = ConflictSetNode(rule)
    last_node.add_child(conflict_set_node, conflict_set_node.activate)
