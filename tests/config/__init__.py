# tests/config/__init__.py

from .settings_config import (
    load_tests_settings,
    validate_tests_settings,
)

__all__ = [
    "load_tests_settings",
    "validate_tests_settings",
]
