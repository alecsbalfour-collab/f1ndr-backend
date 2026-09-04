"""
Event definitions for watchr.
Defines the shape of watcher/trigger events.
"""

from typing import Dict, Any


def build_event(event_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "type": event_type.lower(),
        "data": data,
        "status": "pending",
    }


def event_defaults() -> Dict[str, Any]:
    return {
        "price_change": {"fields": ["id", "old_price", "new_price"]},
        "new_listing": {"fields": ["id", "title", "price", "url"]},
        "listing_update": {"fields": ["id", "changes"]},
        "match_found": {"fields": ["id", "query", "score"]},
    }
