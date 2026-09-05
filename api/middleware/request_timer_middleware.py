import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from logging import getLogger

logger = getLogger("api.timer")


class RequestTimerMiddleware(BaseHTTPMiddleware):
    """
    Measures request execution time and logs it.
    """

    async def dispatch(self, request: Request, call_next):
        start = time.time()

        response = await call_next(request)

        duration_ms = round((time.time() - start) * 1000, 2)
        logger.info(f"{request.method} {request.url.path} took {duration_ms}ms")

        response.headers["X-Process-Time-ms"] = str(duration_ms)

        return response
