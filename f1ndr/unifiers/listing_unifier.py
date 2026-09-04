"""
Listing Unifier
Converts raw scraper dicts into the unified f1ndr listing schema.
"""

from f1ndr.unifiers.field_maps import FIELD_MAPS
from f1ndr.core.helpers_core import safe_str, safe_float


class ListingUnifier:
    """
    Unifies raw listing dicts from any scraper into the standard f1ndr format.
    """

    def unify(self, raw: dict, source: str):
        mapping = FIELD_MAPS.get(source, {})
        unified = {}

        # Apply field mappings
        for unified_key, raw_key in mapping.items():
            unified[unified_key] = safe_str(raw.get(raw_key, ""))

        # Standard fields
        unified["source"] = source
        unified["title"] = unified.get("title", "")
        unified["price"] = safe_float(unified.get("price", 0))
        unified["url"] = unified.get("url", "")
        unified["location"] = unified.get("location", "")
        unified["posted"] = unified.get("posted", "")
        unified["category"] = unified.get("category", "")
        unified["image"] = unified.get("image", "")

        return unified
