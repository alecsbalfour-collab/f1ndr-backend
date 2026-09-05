import pytest
from sellr.core.service_core import ListingService
from sellr.db.listing_repo import ListingRepo

class FakeRepo(ListingRepo):
    def __init__(self):
        self.items = []

    async def insert_listing(self, listing):
        self.items.append(listing)

    async def get_listings(self, query):
        return self.items

@pytest.mark.asyncio
async def test_create_listing():
    repo = FakeRepo()
    service = ListingService(repo)
    result = await service.create_listing({"title": "Bike", "price": 100})
    assert result["success"] is True
