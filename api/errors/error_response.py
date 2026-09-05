from typing import Any, Dict
from fastapi.responses import JSONResponse


def error_response(message: str, status_code: int = 400, details: Dict[str, Any] | None = None) -> JSONResponse:
    """
    Unified error response builder.
    Used by middleware and exception handlers.
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "message": message,
                "details": details or {},
            }
        },
    )
