"""Tests related to `primitives.Callable` function."""
from primitives import Callable
from primitives.exceptions import PrimitiveError  # noqa: F401


def test_empty_callable_object():
    """Empty `Callable` object should return null.

    An object is callable when return value was not specified.

    """
    func = Callable()
    assert func() is None
