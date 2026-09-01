from backend.mongo.mongo_client import mongo

class UserPrefsRepo:
    def __init__(self):
        self.col = mongo["user_prefs"]

    def set_pref(self, user_id: str, key: str, value):
        self.col.update_one(
            {"user_id": user_id},
            {"$set": {key: value}},
            upsert=True
        )

    def get_prefs(self, user_id: str):
        doc = self.col.find_one({"user_id": user_id}, {"_id": 0})
        return doc or {}
