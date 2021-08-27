# Callable

`Callable` fake object is an easy way to reproduce behavior of a function or a
method.

## Principles

- [Empty `Callable` object returns none](#empty-callable-object-returns-none)
- [`Callable` object could return a value](#callable-object-could-return-a-value)
- [`Callable` object should have one or none return value](#callable-object-should-have-one-or-none-return-value)
- [`Callable` object could check passed positional arguments](#callable-object-could-check-passed-positional-arguments)
- [`Callable` object would check arity of the call](#callable-object-would-check-arity-of-the-call)
- [`Callable` object could ignore argument values](#callable-object-could-ignore-argument-values)

### Empty `Callable` object returns none

An empty `Callable` object will just return null value.

```pycon

>>> from primitives import Callable

>>> func = Callable()

>>> func()

```

### `Callable` object could return a value

A return value passed to `Callable` constructor will be returned as is when
you'll call the object.

```pycon

>>> func = Callable(1)

>>> func()
1

```

### `Callable` object should have one or none return value

Only one return value could be passed to the `Callable` object at the
initialization.

```pycon

>>> Callable(1, 2)
Traceback (most recent call last):
  ...
_primitives.exceptions.PrimitiveError: 'Callable' object should have only one return value

```

### `Callable` object could check passed positional arguments

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

### `Callable` object would check arity of the call

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

### `Callable` object could ignore argument values

If you would like to check the number of positional arguments passed to the
faked function, you could use `Ignore` object as argument value. The same would
work if you want to check names of keyword arguments passed to the fake function
without attention to the value of arguments.

```pycon

>>> from primitives import Ignore

>>> func = Callable(1, Argument(Ignore()))

>>> func('a')
1

>>> func('b')
1

```

Checks about number of positional arguments and names of keyword arguments would
still apply.

```pycon

>>> func('a', 'b', 'c')
Traceback (most recent call last):
  ...
_primitives.exceptions.PrimitiveError: Called with more arguments than expected

```

<p align="center">&mdash; ⭐ &mdash;</p>
<p align="center"><i>The <code>primitives</code> library is part of the SOLID python family.</i></p>
