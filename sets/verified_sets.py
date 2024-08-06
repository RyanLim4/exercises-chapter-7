"""Verified sets module."""

from numbers import Integral
from collections.abc import Iterable


class UniquenessError(KeyError):
    pass


class VerifiedSet(set):
    """A base class containing methods common to verified sets.

    Each subclass represents a set which passes a test
    """
    def __init__(self, s):
        self._verify(s)
        super().__init__(s)

    def _verify(self, s):
        raise NotImplementedError

    def add(self, n):
        self._verify(n)
        super().add(n)

    def update(self, s):
        self._verify(s)
        super().update(s)

    def symmetric_difference_update(self, s):
        self._verify(s)
        super().symmetric_difference_update(s)

    def union(self, s):
        self._verify(s)
        return type(self)(super().union(s))

    def intersection(self, s):
        self._verify(s)
        return type(self)(super().intersection(s))

    def difference(self, s):
        self._verify(s)
        return type(self)(super().difference(s))

    def symmetric_difference(self, s):
        self._verify(s)
        return type(self)(super().symmetric_difference(s))

    def copy(self):
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
    """Set where values can only be added if they are not already in the set"""
    def _verify(self, s):
        if isinstance(s, Iterable):
            if any(i in self for i in s):
                raise UniquenessError
        elif s in self:
            raise UniquenessError
