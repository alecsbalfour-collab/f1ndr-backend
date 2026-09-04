"""
General-purpose dict utilities for trinn.
"""

from typing import Dict, Any


def merge_dicts(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    merged = a.copy()
    merged.update(b)
    return merged


def safe_get(d: Dict[str, Any], key: str, default=None):
    return d.get(key, default)
