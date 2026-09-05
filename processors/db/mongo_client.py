from pymongo import MongoClient


class MongoClientWrapper:
    def __init__(self, uri: str = "mongodb://localhost:27017", db_name: str = "f1ndr"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]


mongo_client = MongoClientWrapper()
