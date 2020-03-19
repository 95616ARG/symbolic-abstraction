"""Definitions for the Intervals abstract space.

TODO
"""
from core.abstract import AbstractState

class ReducedProductAbstractState(AbstractState):
    """Abstract state describing the signs of a collection of variables.
    """

    def __init__(self, state_A, state_B):
        """Initializer for the IntervalAbstractState.

        @variable_intervals should be {"variable_name": (lower, upper)}, where
        @lower, @upper are integers. float("+inf") and float("-inf") should be
        used for +/- infinity.
        """
        self.state_A = state_A
        self.state_B = state_B

    def copy(self):
        """Returns a new IntervalAbstractState with the same intervals as self.
        """
        return ReducedProductAbstractState(self.state_A.copy(), self.state_B.copy())

    def __le__(self, rhs):
        """True if self represents a subset of rhs.

        Note that this definition means (not (a <= b)) does NOT imply a > b.
        Perhaps we should raise an exception when elements are uncomparable.
        This assumes that both have the exact same set of variables, and does
        not check that condition.
        """
        return self.state_A <= rhs.state_A and self.state_B <= rhs.state_B

    def translate(self, translation):
        return ReducedProductAbstractState(self.state_A.translate(translation),
                                           self.state_B.translate(translation))

    def __str__(self):
        return str(self.state_A) + "\n" + str(self.state_B)
