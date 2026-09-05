# f1ndr-backend/unifiers/utils/normalize_utils.py
"""
Unifiers normalize utilities.
"""

def normalize_title(title: str) -> str:
    if not title:
        return ""
    return title.strip()
