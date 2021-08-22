"""Tests related to `primitives.Callable` object."""
import pytest

from primitives import Argument
from primitives import Callable
from primitives.exceptions import PrimitiveError


def test_callable_object_return_null():
    """Empty `Callable` object should return null.

    A callable object is empty when return value was not specified.

    """
    func = Callable()
    assert func() is None


def test_callable_object_return_value():
    """`Callable` object should return value passed to it constructor."""
    func = Callable("Hello, John")
    assert func() == "Hello, John"


def test_callable_object_misconfigured():
    """`Callable` object should protect from multiple return values."""
    with pytest.raises(PrimitiveError) as exc_info:
        Callable(1, 2)

    assert str(exc_info.value) == "'Callable' object should have only one return value"


def test_callable_object_null_argument():
    """`Callable` object should return null even if `Argument` was passed."""
    func = Callable(Argument("John"))
    assert func("John") is None

    with pytest.raises(PrimitiveError) as exc_info:
        func("Kate")

    assert str(exc_info.value) == "Called with argument 'Kate' while expected 'John'"


def test_callable_object_return_value_argument():
    """`Callable`object should return value even if `Argument` was passed."""
    func = Callable("Hello, John", Argument("John"))
    assert func("John") == "Hello, John"

    with pytest.raises(PrimitiveError) as exc_info:
        func("Kate")

    assert str(exc_info.value) == "Called with argument 'Kate' while expected 'John'"


def test_callable_object_positional_argument_prevent_keyword():
    """Positional `Argument` should provent usage of keyword argument."""
    func = Callable(Argument("John"))

    with pytest.raises(PrimitiveError) as exc_info:
        func(a="John")

    assert str(exc_info.value) == "Positional arguments can not be called as keyword"


def test_callable_object_positional_argument_not_enough():
    """Raise error if mock specified more arguments than user passed."""
    func = Callable(Argument("John"), Argument("Kate"))

    with pytest.raises(PrimitiveError) as exc_info:
        func("John")

    assert str(exc_info.value) == "Called with less arguments than expected"


def test_callable_object_positional_argument_overflow():
    """Raise error if user passed more arguments than mock specified."""
    func = Callable(Argument("John"))

    with pytest.raises(PrimitiveError) as exc_info:
        func("John", 1)

    assert str(exc_info.value) == "Called with more arguments than expected"
