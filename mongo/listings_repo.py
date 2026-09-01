from mongo.mongo_client import mongo

class ListingsRepo:
    def __init__(self):
        self.col = mongo["listings"]

    def save_many(self, listings: list):
        if listings:
            self.col.insert_many(listings, ordered=False)

    def get_all(self):
        return list(self.col.find({}, {"_id": 0}))

    def clear(self):
        self.col.delete_many({})
