"""Tests related to primitives.func function."""
import pytest

from primitives import func
from primitives.exceptions import PrimitiveError


def test_func():
    """`func` should raise `PrimitiveError`."""
    with pytest.raises(PrimitiveError):
        func()
