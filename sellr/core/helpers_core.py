"""
Sellr helper utilities.
"""

def safe_get(data: dict, key: str, default=None):
    return data.get(key, default)
