from pymongo import MongoClient

class LisTrMongoClient:
    def __init__(self, uri="mongodb://localhost:27017", db_name="listr_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    @property
    def posts(self):
        return self.db["posts"]

    @property
    def validations(self):
        return self.db["validations"]
