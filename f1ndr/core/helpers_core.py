"""
Helper functions for f1ndr.
"""

def safe_str(value):
    if value is None:
        return ""
    return str(value).strip()


def safe_float(value, default=0.0):
    try:
        return float(str(value).replace(",", "").strip())
    except:
        return default
