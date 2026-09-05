# f1ndr-backend/unifiers/data/unifier_data.py
"""
Unifiers unified listing data utilities.
"""

from unifiers.utils.normalize_utils import normalize_title
from unifiers.utils.transform_utils import map_source_to_canonical


def build_unified_listing(transformed: dict) -> dict:
    return {
        "id": transformed.get("id"),
        "title": normalize_title(transformed.get("title")),
        "price": transformed.get("price"),
        "location": transformed.get("location"),
        "platform": map_source_to_canonical(transformed.get("canonical_source")),
    }
