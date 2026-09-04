"""
Service layer for wchtr.
Coordinates watchers, triggers, subscriptions, and event routing.
No engines. No processors. Pure event orchestration.
"""

from typing import Dict, Any
from .helpers import safe_get
from .exceptions import UnknownEventError


class WachtrService:
    def __init__(self):
        # In-memory subscription registry (db layer will override this)
        self.subscriptions = {}

    def handle_watch_event(self, key: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Called when something changes in the system.
        Example: price change, new listing, updated listing, new match.
        """
        return {
            "watch_key": key,
            "received": payload,
            "status": "watch_event_processed",
        }

    def trigger_event(self, event: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Trigger a downstream event.
        Example: notify user, update f1ndr, update lisTr, update sellr.
        """
        if event not in ["price_change", "new_listing", "match_found", "listing_update"]:
            raise UnknownEventError(event)

        return {
            "event": event,
            "data": data,
            "status": "trigger_dispatched",
        }

    def get_subscriptions(self) -> Dict[str, Any]:
        """
        Return all active watcher subscriptions.
        """
        return {
            "subscriptions": self.subscriptions,
            "count": len(self.subscriptions),
        }
