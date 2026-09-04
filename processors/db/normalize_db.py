"""
Mongo client wrapper for processors.
Provides access to collections used by the processors module.
"""

from pymongo import MongoClient


class ProcessorsMongoClient:
    def __init__(
        self,
        uri: str = "mongodb://localhost:27017",
        db_name: str = "f1ndr_backend"
    ):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    @property
    def normalize_records(self):
        return self.db["normalize_records"]

    @property
    def category_records(self):
        return self.db["category_records"]
