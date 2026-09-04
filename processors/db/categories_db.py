from .mongo_client import ProcessorsMongoClient


class CategoriesDB:
    """
    Mongo-backed persistence for categorized text records.
    """

    def __init__(self, client: ProcessorsMongoClient | None = None):
        self.client = client or ProcessorsMongoClient()

    def save(self, text: str, categories: list):
        self.client.category_records.insert_one({
            "text": text,
            "categories": categories
        })

    def find_by_text(self, text: str):
        return self.client.category_records.find_one({"text": text})

    def all(self):
        return list(self.client.category_records.find())
