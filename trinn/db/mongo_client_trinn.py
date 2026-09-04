"""
Mongo client wrapper for trinn.
Provides access to collections used by the trinn module.
"""

from pymongo import MongoClient


class TrinnMongoClient:
    def __init__(self, uri: str = "mongodb://localhost:27017", db_name: str = "trinn_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    @property
    def transform_logs(self):
        return self.db["transform_logs"]

    @property
    def normalize_logs(self):
        return self.db["normalize_logs"]

    @property
    def enrich_logs(self):
        return self.db["enrich_logs"]
