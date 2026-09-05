from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from errors import APIException, error_response
from logging import getLogger

logger = getLogger("api.error")


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    """
    Global error handler middleware.
    Converts exceptions into unified JSON error responses.
    """

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)

        except APIException as exc:
            logger.error(f"APIException: {exc.message} details={exc.details}")
            return error_response(
                message=exc.message,
                status_code=exc.status_code,
                details=exc.details,
            )

        except Exception as exc:
            logger.exception("Unhandled exception occurred")
            return JSONResponse(
                status_code=500,
                content={
                    "error": {
                        "message": "Internal server error",
                        "details": {"exception": str(exc)},
                    }
                },
            )
