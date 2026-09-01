from pymongo import MongoClient
import os

class MongoDB:
    def __init__(self):
        uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.client = MongoClient(uri)
        self.db = self.client["f1ndr"]

mongo = MongoDB().db
