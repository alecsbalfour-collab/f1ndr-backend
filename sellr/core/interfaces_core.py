"""
Sellr interface definitions.
"""

class RepoInterface:
    async def insert_listing(self, listing: dict):
        raise NotImplementedError

    async def get_listings(self, query: dict):
        raise NotImplementedError

    async def remove_listing(self, listing_id: str):
        raise NotImplementedError
