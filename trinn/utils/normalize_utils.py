# f1ndr-backend/trinn/utils/normalize_utils.py
"""
TRINN normalize utilities.
"""

def normalize_title(title: str) -> str:
    if not title:
        return ""
    return title.strip()
