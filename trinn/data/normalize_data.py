"""
Normalization rules for trinn.
Defines how keys and values should be normalized.
"""

from typing import Dict, Any


def normalize_rules() -> Dict[str, Any]:
    return {
        "key_case": "lower",
        "trim_strings": True,
        "collapse_spaces": True,
    }
