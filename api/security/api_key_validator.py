# api/security/api_key_validator.py

from fastapi import Request
from api.errors.error_handler import raise_api_error
from api.security.api_keys import validate_api_key

class APIKeyValidator:
    @staticmethod
    async def api_key_validator(request: Request):
        api_key = request.headers.get("X-API-Key")

        if not api_key:
            raise_api_error("Missing API key", 401)

        if not validate_api_key(api_key):
            raise_api_error("Invalid API key", 403)

        return True

api_key_validator = APIKeyValidator.api_key_validator
