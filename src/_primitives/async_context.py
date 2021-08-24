class AsyncContext:
    """An object appropriate to fake async context manager."""

    def __init__(self, value=None):
        self.value = value

    async def __aenter__(self):
        return self.value

    async def __aexit__(self, exc_type, exc_value, traceback):
        ...
