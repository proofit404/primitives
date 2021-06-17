"""Tests related to `primitives.Awaitable` object."""
import pytest

from primitives import Awaitable


@pytest.mark.asyncio()
async def test_awaitable_object_return_null():
    """Empty `Awaitable` object should return null.

    An awaitable object is empty when return value was not specified.

    """
    awaitable = Awaitable()
    assert await awaitable is None


@pytest.mark.asyncio()
async def test_awaitable_object_return_value():
    """`Awaitable` object should return value passed to it constructor."""
    awaitable = Awaitable("Hello, John")
    assert await awaitable == "Hello, John"
