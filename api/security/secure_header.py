from fastapi import Response

def apply_secure_headers(response: Response) -> None:
    """
    Apply basic security headers.
    Expand later with CSP, HSTS, etc.
    """
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
