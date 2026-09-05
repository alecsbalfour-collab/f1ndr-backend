import pytest
import asyncio
from scrapers.scrapers.marketplace_scraper import run

@pytest.mark.asyncio
async def test_marketplace_run():
    result = await run("chair")
    assert "success" in result
    assert "listings" in result
    assert isinstance(result["listings"], list)
