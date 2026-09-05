import pytest
import asyncio
from scrapers.scrapers.rentfaster_scraper import run

@pytest.mark.asyncio
async def test_rentfaster_run():
    result = await run("condo")
    assert "success" in result
    assert "listings" in result
    assert isinstance(result["listings"], list)
