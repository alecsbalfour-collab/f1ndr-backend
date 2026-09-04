"""
Default watcher intervals for watchr.
These values define how often each watcher runs.
"""

def watcher_intervals():
    return {
        "price_change": 30,      # seconds
        "new_listing": 45,
        "listing_update": 60,
        "match_found": 20,
    }
