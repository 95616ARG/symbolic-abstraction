"""Definitions for abstract state types.
"""

# pylint: disable=too-few-public-methods
class AbstractState:
    """Describes a collection of concrete states.

    The following method should be overridden by sub-classes:
        __le__

    The other methods take their values from __le__.
    """
    def __le__(self, rhs):
        """True if self is exactly a subset of rhs.

        NOTE that this definition means (not (a <= b)) does NOT imply a > b.
        Perhaps we should raise an exception when elements are uncomparable.

        ``Exactly" here means that:
        self <= rhs
        <->
        (domain.gamma_hat(self) -> domain.gamma_hat(rhs))
        """
        raise NotImplementedError

    def __ge__(self, rhs):
        """True if self is a superset of rhs.

        NOTE that this definition means (not (a >= b)) does NOT imply a < b.
        Perhaps we should raise an exception when elements are uncomparable.
        """
        return rhs <= self

    def __eq__(self, rhs):
        """Determines if self and rhs represent the same AbstractState.
        """
        return self <= rhs <= self

    def __ne__(self, rhs):
        """Determines if self and rhs represent different AbstractStates.
        """
        return not self == rhs
