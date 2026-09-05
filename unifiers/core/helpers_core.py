# f1ndr-backend/unifiers/core/helpers_core.py
"""
Unifiers helper utilities.
"""

def safe_get(data: dict, key: str, default=None):
    return data.get(key, default)
