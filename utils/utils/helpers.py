# utils/utils/helpers.py

def clean_text(value: str) -> str:
    """
    Clean and normalize text globally.
    """
    if not isinstance(value, str):
        return value
    return " ".join(value.strip().split()).lower()

def safe_int(value):
    try:
        return int(value)
    except Exception:
        return None

def safe_float(value):
    try:
        return float(value)
    except Exception:
        return None
