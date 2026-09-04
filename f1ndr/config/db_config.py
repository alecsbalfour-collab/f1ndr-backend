class DBConfig:
    """
    MongoDB configuration for f1ndr.
    """

    uri: str = "mongodb://localhost:27017"
    database_name: str = "f1ndr_backend"

    def __init__(self, **overrides):
        for key, value in overrides.items():
            setattr(self, key, value)
