"""
Sellr validation utilities.
"""

def require_fields(data: dict, fields: list):
    missing = [f for f in fields if f not in data]
    return len(missing) == 0
