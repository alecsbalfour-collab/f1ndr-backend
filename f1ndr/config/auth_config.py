class AuthConfig:
    """
    Authentication and security configuration.
    """

    jwt_secret: str = "change_me"
    jwt_expiry_minutes: int = 60
    enable_refresh_tokens: bool = True

    def __init__(self, **overrides):
        for key, value in overrides.items():
            setattr(self, key, value)
