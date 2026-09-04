"""
Subscription registry for watchr.
Tracks user subscriptions to watcher events.
Dict-based, no database logic here.
"""

from typing import Dict, Any, List


class SubscriptionRegistry:
    def __init__(self):
        self.subscriptions: Dict[str, List[Dict[str, Any]]] = {}

    def add(self, user_id: str, event: str, payload: Dict[str, Any]):
        event = event.lower()
        if event not in self.subscriptions:
            self.subscriptions[event] = []

        self.subscriptions[event].append({
            "user_id": user_id,
            "event": event,
            "payload": payload,
        })

    def get(self, event: str) -> List[Dict[str, Any]]:
        return self.subscriptions.get(event.lower(), [])

    def all(self) -> Dict[str, Any]:
        return self.subscriptions
