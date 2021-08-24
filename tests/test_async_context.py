"""Tests related to `primitives.AsyncContext` object."""
import pytest

from primitives import AsyncContext


@pytest.mark.asyncio()
async def test_async_context_object_return_null():
    """Empty `AsyncContext` object should return null.

    An async context object is empty when return value was not specified.

    """
    async_context = AsyncContext()
    async with async_context as result:
        assert result is None


@pytest.mark.asyncio()
async def test_async_context_object_return_value():
    """`AsyncContext` object should return value passed to it constructor."""
    async_context = AsyncContext("Hello, John")
    async with async_context as result:
        assert result == "Hello, John"
