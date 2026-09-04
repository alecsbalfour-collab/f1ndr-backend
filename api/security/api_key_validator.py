from fastapi import Request
from fastapi.exceptions import HTTPException

class APIKeyValidator:
    """
    Optional API key validator for f1ndr API.
    If you decide to enable API keys later, this file is ready.
    """

    def __init__(self, valid_keys: list[str] = None):
        self.valid_keys = valid_keys or []

    def validate(self, request: Request):
        api_key = request.headers.get("X-API-Key")

        if not self.valid_keys:
            # API key system disabled
            return True

        if api_key not in self.valid_keys:
            raise HTTPException(
                status_code=401,
                detail="Invalid or missing API key"
            )

        return True
