from pymongo import MongoClient

class SellrMongoClient:
    def __init__(self, uri="mongodb://localhost:27017", db_name="sellr_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    @property
    def listings(self):
        return self.db["listings"]

    @property
    def updates(self):
        return self.db["updates"]

    @property
    def removals(self):
        return self.db["removals"]
