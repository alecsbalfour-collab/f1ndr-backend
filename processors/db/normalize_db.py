from .mongo_client import mongo_client
from config.normalize_config import normalize_config


class NormalizeDB:
    def __init__(self):
        self.collection = mongo_client.db[normalize_config.collection_name()]

    def store(self, payload: dict) -> dict:
        self.collection.insert_one(payload)
        return payload


normalize_db = NormalizeDB()
