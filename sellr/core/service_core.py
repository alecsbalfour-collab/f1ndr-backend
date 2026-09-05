"""
Sellr service layer.
"""

from sellr.data.listing_data import normalize_listing, validate_listing
from sellr.db.listing_repo import ListingRepo

class ListingService:
    def __init__(self, repo: ListingRepo):
        self.repo = repo

    async def create_listing(self, raw: dict):
        listing = normalize_listing(raw)
        if not validate_listing(listing):
            return {"success": False, "error": "Invalid listing"}

        await self.repo.insert_listing(listing)
        return {"success": True, "listing": listing}

    async def fetch_listings(self, query: dict):
        return await self.repo.get_listings(query)
