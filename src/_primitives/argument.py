from _primitives.exceptions import PrimitiveError


class Argument:
    """An object appropriate to fake function arguments."""

    def __init__(self, value):
        self.value = value

    def check(self, arg):
        """Check argument match."""
        if arg != self.value:
            raise PrimitiveError(
                f"Called with argument {arg!r} while expected {self.value!r}"
            )
