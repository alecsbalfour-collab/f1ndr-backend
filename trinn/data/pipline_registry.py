# f1ndr-backend/trinn/data/normalize_data.py
"""
TRINN normalize data utilities.
"""

def build_normalize_payload(enriched: dict) -> dict:
    base = enriched.get("raw", {})
    return {
        "id": base.get("id"),
        "title": base.get("title"),
        "price": base.get("price"),
        "location": base.get("location"),
        "source": enriched.get("source"),
    }
