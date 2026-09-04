"""
Helper utilities for watchr core.
Dict‑model utilities only.
"""

from typing import Dict, Any


def normalize_key(key: str) -> str:
    return key.strip().lower()


def safe_get(d: Dict[str, Any], key: str, default=None):
    return d.get(key, default)
