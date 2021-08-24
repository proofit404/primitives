# AsyncContext

## Principles

- [Empty `AsyncContext` object returns none](#empty-asynccontext-object-returns-none)

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

<p align="center">&mdash; ⭐ &mdash;</p>
<p align="center"><i>The <code>primitives</code> library is part of the SOLID python family.</i></p>
