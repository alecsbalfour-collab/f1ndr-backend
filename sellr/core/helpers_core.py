"""
Helper functions for sellr.
"""

def safe_field(value):
    if value is None:
        return ""
    return str(value).strip()
