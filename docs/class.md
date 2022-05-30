# Class

`Class` fake object is an easy way to reproduce behavior of classes.

## Principles

- [Empty `Class` object returns a class](#empty-class-object-returns-a-class)

### Empty `Class` object returns a class

An empty `Class` object would just return a class without attributes or methods.

```pycon

>>> from inspect import isclass
>>> from primitives import Class

>>> cls = Class()

>>> isclass(cls)
True

>>> instance = cls()

>>> isinstance(instance, cls)
True

```

<p align="center">&mdash; ⭐ &mdash;</p>
