import pytest
import asyncio
from scrapers.scrapers.used_scraper import run

@pytest.mark.asyncio
async def test_used_run():
    result = await run("tools")
    assert "success" in result
    assert "listings" in result
    assert isinstance(result["listings"], list)
