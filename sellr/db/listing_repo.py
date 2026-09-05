"""
Sellr listing repository.
"""

class ListingRepo:
    def __init__(self, client):
        self.client = client
        self.collection = client["sellr_listings"]

    async def insert_listing(self, listing: dict):
        await self.collection.insert_one(listing)

    async def get_listings(self, query: dict):
        cursor = self.collection.find(query)
        return [doc async for doc in cursor]

    async def remove_listing(self, listing_id: str):
        await self.collection.delete_one({"_id": listing_id})
