from .mongo_client import mongo_client
from config.categories_config import categories_config


class CategoriesDB:
    def __init__(self):
        self.collection = mongo_client.db[categories_config.collection_name()]

    def upsert(self, category: dict) -> dict:
        self.collection.update_one(
            {"slug": category.get("slug")},
            {"$set": category},
            upsert=True,
        )
        return category

    def list_all(self) -> list:
        return list(self.collection.find({}))


categories_db = CategoriesDB()
