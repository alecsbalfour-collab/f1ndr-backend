"""
Watcher definitions for watchr.
These are lightweight dict-based watcher configurations.
"""

from typing import Dict, Any


def build_watcher(key: str, interval: int, description: str = "") -> Dict[str, Any]:
    """
    Create a watcher definition.
    """
    return {
        "key": key.lower(),
        "interval": interval,
        "description": description,
        "active": True,
    }


def watcher_defaults() -> Dict[str, Any]:
    """
    Default watcher set for watchr.
    """
    return {
        "price_change": build_watcher("price_change", 30, "Detects listing price changes"),
        "new_listing": build_watcher("new_listing", 45, "Detects new listings"),
        "listing_update": build_watcher("listing_update", 60, "Detects listing updates"),
        "match_found": build_watcher("match_found", 20, "Detects new matches for saved searches"),
    }
