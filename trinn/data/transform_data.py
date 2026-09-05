# f1ndr-backend/trinn/data/transform_data.py
"""
TRINN transform data utilities.
"""

def build_transform_payload(normalized: dict) -> dict:
    return {
        "id": normalized.get("id"),
        "title": normalized.get("title"),
        "price": normalized.get("price"),
        "location": normalized.get("location"),
        "canonical_source": normalized.get("source"),
    }
