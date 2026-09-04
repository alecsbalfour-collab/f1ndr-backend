"""
Trigger definitions for watchr.
Dict-based trigger routing rules.
"""

from typing import Dict, Any


def build_trigger(event: str, route: str) -> Dict[str, Any]:
    """
    Create a trigger definition.
    """
    return {
        "event": event.lower(),
        "route": route,
        "enabled": True,
    }


def trigger_defaults() -> Dict[str, Any]:
    """
    Default trigger routing table.
    """
    return {
        "price_change": build_trigger("price_change", "notify.user"),
        "new_listing": build_trigger("new_listing", "f1ndr.refresh"),
        "listing_update": build_trigger("listing_update", "f1ndr.update"),
        "match_found": build_trigger("match_found", "notify.user"),
    }
