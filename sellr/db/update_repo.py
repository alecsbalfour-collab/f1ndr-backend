"""
Sellr remove repository.
Handles removal operations for Sellr listings.
"""

class RemoveRepo:
    def __init__(self, client):
        self.client = client
        self.collection = client["sellr_listings"]

    async def remove_by_query(self, query: dict) -> int:
        result = await self.collection.delete_many(query)
        return result.deleted_count

    async def remove_one(self, listing_id: str) -> bool:
        result = await self.collection.delete_one({"_id": listing_id})
        return result.deleted_count == 1
