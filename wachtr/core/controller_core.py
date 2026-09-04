"""
Controller layer for watchr.
Handles incoming watcher/trigger requests and routes them to the service layer.
"""

from typing import Dict, Any, Optional
from .service_core import WatchrService
from .helpers_core import normalize_key


class WatchrController:
    def __init__(self):
        self.service = WatchrService()

    def watch(self, key: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        clean_key = normalize_key(key)
        return self.service.handle_watch_event(clean_key, payload)

    def trigger(self, event: str, data: Dict[str, Any]) -> Dict[str, Any]:
        clean_event = normalize_key(event)
        return self.service.trigger_event(clean_event, data)

    def subscriptions(self) -> Dict[str, Any]:
        return self.service.get_subscriptions()
