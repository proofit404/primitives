# Callable

`Callable` fake object is an easy way to reproduce behavior of a function or a
method.

An empty `Callable` object will just return null value.

```pycon

>>> from primitives import Callable

>>> func = Callable()

>>> func()

```

A return value passed to `Callable` constructor will be returned as is when
you'll call the object.

```pycon

>>> func = Callable(1)

>>> func()
1

```

Only one return value could be passed to the `Callable` object at the
initialization.

```pycon

>>> Callable(1, 2)
Traceback (most recent call last):
  ...
_primitives.exceptions.PrimitiveError: 'Callable' object should have only one return value

```

To make your fake object be able to accept positional arguments, you can pass
`Argument` object at the initialization. An `Argument` object should have
allowed value for this argument to call.

```pycon

>>> from primitives import Argument

>>> func = Callable(1, Argument('a'))

>>> func('a')
1

>>> func('b')
Traceback (most recent call last):
  ...
_primitives.exceptions.PrimitiveError: Called with argument 'b' while expected 'a'

```

If you want your callable fake object to receive arguments but return null, you
can avoid specifying return value explicitly.

```pycon

>>> func = Callable(Argument('a'), Argument('b'))

>>> func('a', 'b')

```

A `Callable` fake object would as well check if amount of passed arguments
matched arity of declared function.

```pycon

>>> func('a')
Traceback (most recent call last):
  ...
_primitives.exceptions.PrimitiveError: Called with less arguments than expected

>>> func('a', 'b', 'c')
Traceback (most recent call last):
  ...
_primitives.exceptions.PrimitiveError: Called with more arguments than expected

```

<p align="center">&mdash; ⭐ &mdash;</p>
<p align="center"><i>The <code>primitives</code> library is part of the SOLID python family.</i></p>
