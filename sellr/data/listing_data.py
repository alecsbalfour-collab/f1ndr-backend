"""
Listing data model and normalization for Sellr.
"""

def normalize_listing(raw: dict) -> dict:
    return {
        "title": raw.get("title"),
        "price": raw.get("price"),
        "url": raw.get("url"),
        "image": raw.get("image"),
        "location": raw.get("location"),
        "platform": raw.get("platform", "sellr"),
    }


def validate_listing(data: dict) -> bool:
    if not data.get("title"):
        return False
    if data.get("price") is None:
        return False
    return True
