class AsyncContext:
    """An object appropriate to fake async context manager."""

    async def __aenter__(self):
        ...

    async def __aexit__(self, exc_type, exc_value, traceback):
        ...
