class AppConfig:
    """
    Core application configuration.
    """

    app_name: str = "f1ndr"
    environment: str = "development"
    debug: bool = True

    def __init__(self, **overrides):
        for key, value in overrides.items():
            setattr(self, key, value)
