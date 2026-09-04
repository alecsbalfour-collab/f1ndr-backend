"""
Utilities for transformation operations.
"""

from typing import Dict, Any


def strip_whitespace(value: Any) -> Any:
    if isinstance(value, str):
        return value.strip()
    return value


def lowercase_keys(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k.lower(): v for k, v in data.items()}


def convert_empty_to_none(value: Any) -> Any:
    if value == "" or value is None:
        return None
    return value
