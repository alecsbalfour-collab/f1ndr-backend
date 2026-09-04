class BaseConfig:
    """
    Shared configuration base for all processors.
    Supports runtime overrides.
    """

    enabled: bool = True
    version: str = "1.0.0"

    def __init__(self, **overrides):
        for key, value in overrides.items():
            setattr(self, key, value)
