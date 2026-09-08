# f1ndr_backend/api/security/rate_limiter.py

from slowapi import Limiter
from slowapi.util import get_remote_address

# Global rate limiter instance
limiter = Limiter(
    key_func=get_remote_address,     # identifies clients by IP
    default_limits=["100/minute"],   # global default limit
)
