"""
Repository for enrichment logs.
Stores enriched results for debugging and auditing.
"""

from typing import Dict, Any
from .mongo_client_trinn import TrinnMongoClient


class EnrichRepo:
    def __init__(self, client: TrinnMongoClient):
        self.collection = client.enrich_logs

    def log(self, payload: Dict[str, Any], output: Dict[str, Any]):
        entry = {
            "input": payload,
            "output": output,
            "status": "enriched"
        }
        self.collection.insert_one(entry)
        return entry

    def all(self):
        return list(self.collection.find({}))
