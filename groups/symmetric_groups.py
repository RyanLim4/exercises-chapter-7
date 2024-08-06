"""A module providing symmetric groups."""
from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    """The general symmetric group."""
    symbol = "S"

    def _validate(self, value):
        """Ensure that value is an allowed element value in this group."""
        value = np.asarray(value)
        if not (value.shape == (self.n,)):
            raise ValueError("Element must be a "
                             f"1 x {self.n}"
                             "array.")
        if any(i not in value for i in range(self.n)):
            raise ValueError(f"Element must contain {{0, ..., {self.n-1} }}")

    def operation(self, a, b):
        """Perform the group operation on 2 values.

        The group operation is function composition.
        """
        return a[b]
