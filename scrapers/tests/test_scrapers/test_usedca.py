import pytest
import asyncio
from scrapers.scrapers.usedca_scraper import run

@pytest.mark.asyncio
async def test_usedca_run():
    result = await run("furniture")
    assert "success" in result
    assert "listings" in result
    assert isinstance(result["listings"], list)
