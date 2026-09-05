# f1ndr-backend/unifiers/data/normalize_data.py
"""
Unifiers normalize data utilities.
"""

def build_normalize_payload(raw: dict) -> dict:
    return {
        "id": raw.get("id"),
        "title": raw.get("title"),
        "price": raw.get("price"),
        "location": raw.get("location"),
        "source": raw.get("source"),
    }
