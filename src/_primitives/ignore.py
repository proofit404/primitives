class Ignore:
    """An object appropriate to ignore function arguments."""

    def __ne__(self, other):
        return False
