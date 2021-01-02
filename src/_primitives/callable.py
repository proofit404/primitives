from _primitives.argument import Argument
from _primitives.exceptions import PrimitiveError


class Callable:
    """An object appropriate to fake functions and methods."""

    def __init__(self, *args):
        arguments, values = _arguments(args)
        self.check = _Check(arguments)
        self.return_value = _return_value(values)

    def __call__(self, *args, **kwargs):
        """Return predefined value."""
        self.check(args, kwargs)
        return self.return_value


def _arguments(args):
    arguments = []
    values = []
    for arg in args:
        if isinstance(arg, Argument):
            arguments.append(arg)
        else:
            values.append(arg)
    return arguments, values


def _return_value(args):
    if len(args) > 1:
        raise PrimitiveError("'Callable' object should have only one return value")
    elif args:
        return args[0]


class _Check:
    def __init__(self, arguments):
        self.arguments = arguments

    def __call__(self, args, kwargs):
        if kwargs:
            raise PrimitiveError("Positional arguments can not be called as keyword")
        iterator = _Iterator(args)
        for argument in self.arguments:
            value = iterator.get()
            argument.check(value)
        iterator.last()


class _Iterator:
    def __init__(self, args):
        self.state = iter(args)

    def get(self):
        try:
            return next(self.state)
        except StopIteration:
            raise PrimitiveError("Called with less arguments than expected")

    def last(self):
        try:
            next(self.state)
        except StopIteration:
            pass
        else:
            raise PrimitiveError("Called with more arguments than expected")
