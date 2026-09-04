# tests/Db/__init__.py

from .connection_db import (
    get_tests_connection,
    ping_tests_connection,
)

__all__ = [
    "get_tests_connection",
    "ping_tests_connection",
]
