"""
Sellr controller layer.
"""

from sellr.core.service_core import ListingService

class ListingController:
    def __init__(self, service: ListingService):
        self.service = service

    async def create(self, payload: dict):
        return await self.service.create_listing(payload)

    async def list(self, query: dict):
        return await self.service.fetch_listings(query)
