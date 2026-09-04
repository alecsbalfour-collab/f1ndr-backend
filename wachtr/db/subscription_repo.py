"""
Repository for watcher subscriptions.
Stores user subscriptions to watcher events.
"""

from typing import Dict, Any, List
from .mongo_client_watchr import WatchrMongoClient


class SubscriptionRepo:
    def __init__(self, client: WatchrMongoClient):
        self.collection = client.subscriptions

    def add(self, user_id: str, event: str, payload: Dict[str, Any]):
        entry = {
            "user_id": user_id,
            "event": event.lower(),
            "payload": payload
        }
        self.collection.insert_one(entry)
        return entry

    def get(self, event: str) -> List[Dict[str, Any]]:
        return list(self.collection.find({"event": event.lower()}))

    def all(self):
        return list(self.collection.find({}))
