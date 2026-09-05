class AuthConfig:
    secret_key: str = "change-me"
    token_expiry_minutes: int = 60

auth_config = AuthConfig()
