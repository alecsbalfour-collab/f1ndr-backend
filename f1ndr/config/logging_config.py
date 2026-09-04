class LoggingConfig:
    """
    Logging configuration for f1ndr.
    """

    level: str = "INFO"
    json_output: bool = False

    def __init__(self, **overrides):
        for key, value in overrides.items():
            setattr(self, key, value)
