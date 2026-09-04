"""
Tests for watchr.db repositories.
These tests use in-memory mocks instead of a real Mongo instance.
"""

from watchr.db.watcher_state_repo import WatcherStateRepo
from watchr.db.event_log_repo import EventLogRepo
from watchr.db.subscription_repo import SubscriptionRepo


class MockCollection:
    def __init__(self):
        self.data = []

    def find_one(self, query):
        for item in self.data:
            if item.get("key") == query.get("key"):
                return item
        return None

    def update_one(self, query, update, upsert=False):
        existing = self.find_one(query)
        if existing:
            existing.update(update["$set"])
        else:
            new_item = {"key": query["key"], **update["$set"]}
            self.data.append(new_item)

    def insert_one(self, entry):
        self.data.append(entry)

    def find(self, query):
        if not query:
            return self.data
        return [item for item in self.data if item.get("event") == query.get("event")]


class MockClient:
    def __init__(self):
        self.watcher_state = MockCollection()
        self.event_logs = MockCollection()
        self.subscriptions = MockCollection()


def test_watcher_state_repo():
    repo = WatcherStateRepo(MockClient())
    repo.update("price_change", {"last": 123})

    result = repo.get("price_change")
    assert result["last"] == 123


def test_event_log_repo():
    repo = EventLogRepo(MockClient())
    entry = repo.log("new_listing", {"id": "1"})

    assert entry["event"] == "new_listing"
    assert entry["data"]["id"] == "1"


def test_subscription_repo():
    repo = SubscriptionRepo(MockClient())
    repo.add("user123", "match_found", {"id": "abc"})

    results = repo.get("match_found")
    assert len(results) == 1
    assert results[0]["user_id"] == "user123"
