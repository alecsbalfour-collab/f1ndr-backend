# f1ndr-backend/trinn/utils/transform_utils.py
"""
TRINN transform utilities.
"""

def map_source_to_canonical(source: str) -> str:
    if not source:
        return "unknown"
    return source.lower()
