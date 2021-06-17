class Awaitable:
    """An object appropriate to fake coroutines and futures."""

    def __init__(self, value=None):
        self.value = value

    def __await__(self):
        if False:  # pragma: no cover
            yield
        return self.value
