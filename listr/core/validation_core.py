"""
Validation helpers.
"""

def is_valid_title(title: str):
    return bool(title and len(title.strip()) > 0)
