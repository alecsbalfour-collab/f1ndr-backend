# f1ndr-backend/unifiers/utils/transform_utils.py
"""
Unifiers transform utilities.
"""

def map_source_to_canonical(source: str) -> str:
    if not source:
        return "unknown"
    return source.lower()
