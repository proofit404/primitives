# Awaitable

## Principles

- [Empty `Awaitable` object returns none](#empty-awaitable-object-returns-none)
- [Value passed to `Awaitable` object would be returned](#value-passed-to-awaitable-object-would-be-returned)
- [`Awaitable` object could be returned by `Callable` object](#awaitable-object-could-be-returned-by-callable-object)

### Empty `Awaitable` object returns none

```pycon

>>> import asyncio
>>> from primitives import Awaitable

>>> awaitable = Awaitable()

>>> async def check():
...     return await awaitable

>>> asyncio.run(check())

```

### Value passed to `Awaitable` object would be returned

```pycon

>>> awaitable = Awaitable(1)

>>> asyncio.run(check())
1

```

### `Awaitable` object could be returned by `Callable` object

```pycon

>>> from primitives import Callable

>>> coro = Callable(Awaitable(1))

>>> async def check():
...     return await coro()

>>> asyncio.run(check())
1

```

<p align="center">&mdash; ⭐ &mdash;</p>
<p align="center"><i>The <code>primitives</code> library is part of the SOLID python family.</i></p>
