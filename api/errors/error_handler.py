from fastapi import HTTPException
from typing import Any, Dict

class APIException(HTTPException):
    """
    Unified API exception wrapper.
    """
    def __init__(self, status_code: int, message: str, details: Dict[str, Any] | None = None):
        super().__init__(status_code=status_code, detail=message)
        self.message = message
        self.details = details or {}

def raise_api_error(status_code: int, message: str, details: Dict[str, Any] | None = None):
    """
    Helper to raise APIException cleanly.
    """
    raise APIException(status_code=status_code, message=message, details=details)

def error_response(message: str, status_code: int = 400):
    """
    Middleware-friendly error response.
    """
    return {
        "error": {
            "message": message,
            "status_code": status_code
        }
    }
