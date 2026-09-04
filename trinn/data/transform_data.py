"""
Default transformation rules for trinn.
These are simple dict-based transformation definitions.
"""

from typing import Dict, Any


def transform_rules() -> Dict[str, Any]:
    return {
        "strip_whitespace": True,
        "lowercase_keys": True,
        "convert_empty_to_none": True,
    }
