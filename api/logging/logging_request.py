import time
from fastapi import Request
from typing import Callable
from .api_logger import api_logger


async def log_request(request: Request, call_next: Callable):
    """
    Logs incoming requests and their execution time.
    This is used by middleware.
    """
    start_time = time.time()

    response = await call_next(request)

    duration = round((time.time() - start_time) * 1000, 2)

    api_logger.info(
        f"{request.method} {request.url.path} completed in {duration}ms "
        f"status={response.status_code}"
    )

    return response
