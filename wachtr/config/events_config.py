"""
Event field definitions for watchr.
Defines the required fields for each event type.
"""

def event_fields():
    return {
        "price_change": ["id", "old_price", "new_price"],
        "new_listing": ["id", "title", "price", "url"],
        "listing_update": ["id", "changes"],
        "match_found": ["id", "query", "score"],
    }
