# f1ndr-backend/trinn/core/helpers_core.py
"""
TRINN helper utilities.
"""

def safe_get(data: dict, key: str, default=None):
    return data.get(key, default)
