class Instance:
    """An object appropriate to fake object instances."""

    def __init__(self, **attributes):
        self.__dict__.update(attributes)
