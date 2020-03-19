"""Definitions for the Intervals abstract space.
"""

from enum import Enum
from core.abstract import AbstractState

class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __le__(self, rhs):
        return (self.lower > self.upper or
                rhs.lower <= self.lower <= self.upper <= rhs.upper)

    def __ge__(self, rhs):
        return rhs <= self

    def __eq__(self, rhs):
        return self <= rhs <= self

    def union(self, other):
        return Interval(min(self.lower, other.lower),
                        max(self.upper, other.upper))

    def intersection(self, other):
        return Interval(max(self.lower, other.lower),
                        min(self.upper, other.upper))

    def __repr__(self):
        return str((self.lower, self.upper))

class IntervalAbstractState(AbstractState):
    """Abstract state describing the signs of a collection of variables.
    """

    def __init__(self, variable_intervals):
        """Initializer for the IntervalAbstractState.

        @variable_intervals should be {"variable_name": (lower, upper)}, where
        @lower, @upper are integers. float("+inf") and float("-inf") should be
        used for +/- infinity.
        """
        self.variable_intervals = variable_intervals
        self.variables = list(variable_intervals.keys())

    def copy(self):
        """Returns a new IntervalAbstractState with the same intervals as self.
        """
        return IntervalAbstractState(self.variable_intervals.copy())

    def interval_of(self, variable_name):
        """Returns the Interval of a variable given its name.
        """
        return self.variable_intervals[variable_name]

    def set_interval(self, variable_name, interval):
        """Sets the interval of a variable given its name.
        """
        self.variable_intervals[variable_name] = interval

    def __le__(self, rhs):
        """True if self represents a subset of rhs.

        Note that this definition means (not (a <= b)) does NOT imply a > b.
        Perhaps we should raise an exception when elements are uncomparable.
        This assumes that both have the exact same set of variables, and does
        not check that condition.
        """
        return all(self.interval_of(name) <= rhs.interval_of(name)
                   for name in self.variables)

    def translate(self, translation):
        return IntervalAbstractState({
            translation[name]: state
            for name, state in self.variable_intervals.items()
        })

    def __str__(self):
        return str(self.variable_intervals)
