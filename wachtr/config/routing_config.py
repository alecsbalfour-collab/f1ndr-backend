"""
Trigger routing configuration for watchr.
Defines where each event should be dispatched.
"""

def routing_table():
    return {
        "price_change": "notify.user",
        "new_listing": "f1ndr.refresh",
        "listing_update": "f1ndr.update",
        "match_found": "notify.user",
    }
