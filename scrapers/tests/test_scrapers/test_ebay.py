import pytest
import asyncio
from scrapers.scrapers.ebay_scraper import run

@pytest.mark.asyncio
async def test_ebay_run():
    result = await run("laptop")
    assert "success" in result
    assert "listings" in result
    assert isinstance(result["listings"], list)
