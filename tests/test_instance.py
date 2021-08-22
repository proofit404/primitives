"""Tests related to `primitives.Instance` object."""
import pytest

from primitives import Awaitable
from primitives import Callable
from primitives import Instance


def test_instance_no_attributes():
    """Empty `Instance` object should not have attributes.

    An instance object is empty when non of the attributes were specified.

    """
    user = Instance()
    assert not hasattr(user, "greet")


def test_instance_method():
    """`Instance` object should give access to methods."""
    user = Instance(greet=Callable("Hello, John"))
    assert user.greet() == "Hello, John"


@pytest.mark.asyncio()
async def test_instance_async_method():
    """`Instance` object should give access to async methods."""
    user = Instance(greet=Callable(Awaitable("Hello, John")))
    assert await user.greet() == "Hello, John"
