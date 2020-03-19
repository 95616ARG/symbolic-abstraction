"""Module containing definitions for the Interval domain.

This domain has an abstract space consisting of bottom, strictly positive,
strictly negative, or top states for each variable in a program. The logical
space is the set of conjunctions of one-variable inequalities against 0.
"""
from .abstract import Interval, IntervalAbstractState
from .domain import IntervalDomain
