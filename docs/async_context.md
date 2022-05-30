# AsyncContext

`AsyncContext` fake object is an easy way to reproduce behavior of asynchronous
context managers.

## Principles

- [Empty `AsyncContext` object returns none](#empty-asynccontext-object-returns-none)
- [Value passed to `AsyncContext` object would be returned](#value-passed-to-asynccontext-object-would-be-returned)
- [`AsyncContext` object could be returned by `Callable` object](#asynccontext-object-could-be-returned-by-callable-object)

### Empty `AsyncContext` object returns none

```pycon

>>> import asyncio
>>> from primitives import AsyncContext

>>> async def check():
...     async with resourse as result:
...         return result

>>> resourse = AsyncContext()

>>> asyncio.run(check())

```

### Value passed to `AsyncContext` object would be returned

```pycon

>>> async def check():
...     async with resourse as result:
...         return result

>>> resourse = AsyncContext(1)

>>> asyncio.run(check())
1

```

### `AsyncContext` object could be returned by `Callable` object

```pycon

>>> from primitives import Callable, Argument

>>> async def check():
...     async with resourse('John') as result:
...         return result

>>> resourse = Callable(AsyncContext(1), Argument('John'))

>>> asyncio.run(check())
1

```

<p align="center">&mdash; ⭐ &mdash;</p>
