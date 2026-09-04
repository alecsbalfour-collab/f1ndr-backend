"""
Repository for normalization logs.
Stores normalized results for debugging and auditing.
"""

from typing import Dict, Any
from .mongo_client_trinn import TrinnMongoClient


class NormalizeRepo:
    def __init__(self, client: TrinnMongoClient):
        self.collection = client.normalize_logs

    def log(self, payload: Dict[str, Any], output: Dict[str, Any]):
        entry = {
            "input": payload,
            "output": output,
            "status": "normalized"
        }
        self.collection.insert_one(entry)
        return entry

    def all(self):
        return list(self.collection.find({}))
