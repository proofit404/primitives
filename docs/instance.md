# Instance

`Instance` fake object is an easy way to reproduce behavior of any object
together with its attributes and methods.

## Principles

- [Empty `Instance` object does not have attributes](#empty-instance-object-does-not-have-attributes)
- [`Instance` object provide attribute access to methods](#instance-object-provide-attribute-access-to-methods)
- [`Instance` object provide attribute access to async methods](#instance-object-provide-attribute-access-to-async-methods)

### Empty `Instance` object does not have attributes

```pycon

>>> from primitives import Instance, Callable, Argument, Awaitable

>>> user = Instance()

>>> hasattr(user, "greet")
False

```

### `Instance` object provide attribute access to methods

```pycon

>>> user = Instance(greet=Callable('Hello, John', Argument('John')))

>>> user.greet('John')
'Hello, John'

```

### `Instance` object provide attribute access to async methods

```pycon

>>> import asyncio

>>> user = Instance(greet=Callable(Awaitable('Hello, John'), Argument('John')))

>>> async def check():
...     return await user.greet('John')

>>> asyncio.run(check())
'Hello, John'

```

<p align="center">&mdash; ⭐ &mdash;</p>
