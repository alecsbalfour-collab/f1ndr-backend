from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.errors.api_exceptions import APIError
from api.errors.error_response import ErrorResponse


def add_error_handler_middleware(app: FastAPI):
    @app.exception_handler(APIError)
    async def api_error_handler(request: Request, exc: APIError):
        return JSONResponse(
            status_code=exc.status_code,
            content=ErrorResponse(
                error="APIError",
                message=exc.message,
                details=exc.details,
                request_id=getattr(request.state, "request_id", None),
            ).dict(),
        )

    @app.exception_handler(Exception)
    async def generic_error_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                error="InternalServerError",
                message=str(exc),
                details=None,
                request_id=getattr(request.state, "request_id", None),
            ).dict(),
        )
