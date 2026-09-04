"""
Repository for watcher state.
Tracks last-run timestamps, last-known values, and active watchers.
"""

from typing import Dict, Any
from .mongo_client_watchr import WatchrMongoClient


class WatcherStateRepo:
    def __init__(self, client: WatchrMongoClient):
        self.collection = client.watcher_state

    def get(self, key: str) -> Dict[str, Any]:
        return self.collection.find_one({"key": key.lower()}) or {}

    def update(self, key: str, data: Dict[str, Any]):
        self.collection.update_one(
            {"key": key.lower()},
            {"$set": data},
            upsert=True
        )

    def all(self):
        return list(self.collection.find({}))
