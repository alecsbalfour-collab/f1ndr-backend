import pytest
import asyncio
from scrapers.scrapers.craigslist_scraper import run

@pytest.mark.asyncio
async def test_craigslist_run():
    result = await run("bike")
    assert "success" in result
    assert "listings" in result
    assert isinstance(result["listings"], list)
