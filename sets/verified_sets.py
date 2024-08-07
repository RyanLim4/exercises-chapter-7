"""Verified sets module."""

from numbers import Integral
from collections.abc import Iterable


class UniquenessError(KeyError):
    """Error for UniqueSet class."""

    pass


class VerifiedSet(set):
    """A base class containing methods common to verified sets.

    Each subclass represents a set which passes a test
    """

    def __init__(self, s):
        """Construct a VerifiedSet object."""
        self._verify(s)
        super().__init__(s)

    def _verify(self, s):
        raise NotImplementedError

    def add(self, n):
        """Add an element to a VerifiedSet."""
        self._verify(n)
        super().add(n)

    def update(self, s):
        """Add elements to a VerifiedSet."""
        self._verify(s)
        super().update(s)

    def symmetric_difference_update(self, s):
        """Get symmetric difference of a set with other sets."""
        self._verify(s)
        super().symmetric_difference_update(s)

    def union(self, s):
        """Return Union of sets."""
        self._verify(s)
        return type(self)(super().union(s))

    def intersection(self, s):
        """Return intersections of sets."""
        self._verify(s)
        return type(self)(super().intersection(s))

    def difference(self, s):
        """Return set difference."""
        self._verify(s)
        return type(self)(super().difference(s))

    def symmetric_difference(self, s):
        """Return symmetric set difference."""
        self._verify(s)
        return type(self)(super().symmetric_difference(s))

    def copy(self):
        """Return a copy of the set."""
        return type(self)(super().copy())


class IntSet(VerifiedSet):
    """A set that only contains integers."""

    def _verify(self, s):
        if isinstance(s, Iterable):
            for val in s:
                if not isinstance(val, Integral):
                    raise TypeError("IntSet expected an integer, got a "
                                    + type(val).__name__)
        elif not isinstance(s, Integral):
            raise TypeError("IntSet expected an integer, got a "
                            + type(val).__name__)


class UniqueSet(VerifiedSet):
    """Set where repeats cannot be added."""

    def _verify(self, s):
        if isinstance(s, Iterable):
            if any(i in self for i in s):
                raise UniquenessError
        elif s in self:
            raise UniquenessError
