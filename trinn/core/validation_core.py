"""
Validation utilities for trinn.
Dict‑based. No Pydantic.
"""

from typing import Dict, Any


def validate_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "valid": isinstance(data, dict),
        "fields": list(data.keys()),
        "payload": data
    }
