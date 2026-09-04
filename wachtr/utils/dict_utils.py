"""
General-purpose dict utilities for watchr.
"""

from typing import Dict, Any


def merge_dicts(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dicts, with b overwriting a.
    """
    merged = a.copy()
    merged.update(b)
    return merged


def safe_get(d: Dict[str, Any], key: str, default=None):
    return d.get(key, default)
