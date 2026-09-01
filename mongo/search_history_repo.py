from mongo.mongo_client import mongo
from datetime import datetime

class SearchHistoryRepo:
    def __init__(self):
        self.col = mongo["search_history"]

    def log(self, query: str, platforms: list):
        self.col.insert_one({
            "query": query,
            "platforms": platforms,
            "timestamp": datetime.utcnow()
        })

    def get_recent(self, limit=20):
        return list(
            self.col.find({}, {"_id": 0})
                .sort("timestamp", -1)
                .limit(limit)
        )
