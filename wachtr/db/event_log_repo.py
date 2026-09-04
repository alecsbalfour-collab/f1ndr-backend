"""
Repository for event logs.
Stores triggered events for auditing and debugging.
"""

from typing import Dict, Any
from .mongo_client_watchr import WatchrMongoClient


class EventLogRepo:
    def __init__(self, client: WatchrMongoClient):
        self.collection = client.event_logs

    def log(self, event: str, data: Dict[str, Any]):
        entry = {
            "event": event.lower(),
            "data": data,
            "status": "logged"
        }
        self.collection.insert_one(entry)
        return entry

    def get_by_event(self, event: str):
        return list(self.collection.find({"event": event.lower()}))

    def all(self):
        return list(self.collection.find({}))
