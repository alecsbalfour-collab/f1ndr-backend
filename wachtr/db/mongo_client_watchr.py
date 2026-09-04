"""
Mongo client wrapper for watchr.
Provides access to collections used by the watcher module.
"""

from typing import Any
from pymongo import MongoClient


class WatchrMongoClient:
    def __init__(self, uri: str = "mongodb://localhost:27017", db_name: str = "watchr_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    @property
    def watcher_state(self):
        return self.db["watcher_state"]

    @property
    def event_logs(self):
        return self.db["event_logs"]

    @property
    def subscriptions(self):
        return self.db["subscriptions"]
