# f1ndr-backend/trinn/utils/dict_utils.py
"""
TRINN dictionary utilities.
"""

def merge_dicts(base: dict, updates: dict) -> dict:
    merged = base.copy()
    merged.update(updates)
    return merged


def filter_keys(data: dict, allowed: list) -> dict:
    return {k: v for k, v in data.items() if k in allowed}
