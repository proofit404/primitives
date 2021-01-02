class Callable:
    """An object appropriate to fake functions and methods."""

    def __init__(self, *args):
        if args:
            self.return_value = args[0]
        else:
            self.return_value = None

    def __call__(self):
        """Return predefined value."""
        return self.return_value
