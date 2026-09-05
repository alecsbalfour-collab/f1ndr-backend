from fastapi import Request
from errors import raise_api_error

class APIKeyValidator:
    """
    Simple API key validator.
    Expand later with DB-backed keys, roles, scopes, etc.
    """

    def __init__(self, valid_keys: list[str] | None = None):
        self.valid_keys = valid_keys or []

    def validate(self, request: Request) -> None:
        api_key = request.headers.get("X-API-Key")

        if not api_key:
            raise_api_error(
                status_code=401,
                message="Missing API key",
                details={"header": "X-API-Key"},
            )

        if api_key not in self.valid_keys:
            raise_api_error(
                status_code=403,
                message="Invalid API key",
                details={"provided_key": api_key},
            )


api_key_validator = APIKeyValidator(valid_keys=["dev-key"])
