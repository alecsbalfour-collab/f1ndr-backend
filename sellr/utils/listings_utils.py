"""
Listings utilities for Sellr.
Provides normalization, cleaning, and safe conversions for listing fields.
"""

def clean_title(title: str) -> str:
    """
    Normalize and sanitize listing titles.
    """
    if not title:
        return ""
    return title.strip()


def safe_price(value) -> float:
    """
    Convert price-like values into a safe float.
    Returns 0.0 if conversion fails.
    """
    try:
        return float(value)
    except Exception:
        return 0.0


def normalize_listing_fields(raw: dict) -> dict:
    """
    Normalize common listing fields into a consistent DICT structure.
    """
    return {
        "title": clean_title(raw.get("title")),
        "price": safe_price(raw.get("price")),
        "image": raw.get("image"),
        "url": raw.get("url"),
        "location": raw.get("location"),
        "platform": raw.get("platform", "sellr"),
    }


def ensure_defaults(listing: dict) -> dict:
    """
    Apply default values to missing listing fields.
    """
    defaults = {
        "title": "",
        "price": 0.0,
        "image": None,
        "url": None,
        "location": None,
        "platform": "sellr",
    }

    merged = defaults.copy()
    merged.update(listing)
    return merged
