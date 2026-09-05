# f1ndr-backend/unifiers/db/unifier_state.py
"""
Unifiers unified state repository.
"""

class UnifierStateRepo:
    def __init__(self, client):
        self.client = client
        self.collection = client["unifiers_state"]

    async def save_unified(self, doc: dict):
        await self.collection.insert_one(doc)

    async def fetch_unified(self, query: dict):
        cursor = self.collection.find(query)
        return [d async for d in cursor]
