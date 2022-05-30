class Class:
    """An object appropriate to fake classes."""

    def __new__(cls):
        """Build a new class."""
        return type("Class", (), {})
