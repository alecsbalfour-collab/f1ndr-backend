# f1ndr-backend/unifiers/db/normalize_repo.py
"""
Unifiers normalize repository.
"""

class NormalizeRepo:
    def __init__(self, client):
        self.client = client
        self.collection = client["unifiers_normalize"]

    async def insert(self, doc: dict):
        await self.collection.insert_one(doc)

    async def fetch(self, query: dict):
        cursor = self.collection.find(query)
        return [d async for d in cursor]
