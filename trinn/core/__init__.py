# f1ndr-backend/trinn/core/validation_core.py
"""
TRINN validation utilities.
"""

def require_fields(data: dict, fields: list) -> bool:
    missing = [f for f in fields if f not in data]
    return len(missing) == 0
