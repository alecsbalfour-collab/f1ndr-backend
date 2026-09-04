from time import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class RequestTimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time()

        # Process request
        response = await call_next(request)

        # Calculate duration
        duration_ms = round((time() - start) * 1000, 2)

        # Add timing header
        response.headers["X-Response-Time-ms"] = str(duration_ms)

        return response


def add_request_timer_middleware(app):
    app.add_middleware(RequestTimerMiddleware)
