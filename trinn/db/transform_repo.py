# f1ndr-backend/trinn/db/transform_repo.py
"""
TRINN transform repository.
"""

class TransformRepo:
    def __init__(self, client):
        self.client = client
        self.collection = client["trinn_transform"]

    async def insert(self, doc: dict):
        await self.collection.insert_one(doc)

    async def fetch(self, query: dict):
        cursor = self.collection.find(query)
        return [d async for d in cursor]
