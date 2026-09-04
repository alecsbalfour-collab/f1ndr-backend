import logging

def log_request(request, request_id: str):
    """
    Logs incoming API requests with method, path, and request ID.
    """
    logging.info(
        f"[REQUEST] {request.method} {request.url.path} | request_id={request_id}"
    )


def log_response(request_id: str, status_code: int, duration_ms: float):
    """
    Logs outgoing API responses with status code and timing.
    """
    logging.info(
        f"[RESPONSE] status={status_code} duration={duration_ms}ms | request_id={request_id}"
    )
