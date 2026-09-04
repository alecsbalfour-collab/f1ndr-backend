"""
Utilities for normalization operations.
"""

from typing import Dict, Any


def trim_strings(data: Dict[str, Any]) -> Dict[str, Any]:
    out = {}
    for k, v in data.items():
        if isinstance(v, str):
            out[k] = v.strip()
        else:
            out[k] = v
    return out


def collapse_spaces(value: Any) -> Any:
    if isinstance(value, str):
        return " ".join(value.split())
    return value


def normalize_key_case(data: Dict[str, Any], case: str = "lower") -> Dict[str, Any]:
    if case == "lower":
        return {k.lower(): v for k, v in data.items()}
    if case == "upper":
        return {k.upper(): v for k, v in data.items()}
    return data
