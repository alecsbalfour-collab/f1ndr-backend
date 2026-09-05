"""
Sellr remove data utilities.
"""

def build_remove_query(raw: dict) -> dict:
    query = {}

    if "listing_id" in raw:
        query["_id"] = raw["listing_id"]

    if "platform" in raw:
        query["platform"] = raw["platform"]

    if "location" in raw:
        query["location"] = raw["location"]

    return query
