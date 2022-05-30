"""Tests related to `primitives.Class` function."""
from inspect import isclass

from primitives import Class


def test_empty_class_object():
    """Empty `Class` object should return a class."""
    cls = Class()
    assert isclass(cls)
    assert cls.__name__ == "Class"
