import pytest
import asyncio
from scrapers.scrapers.facebook_scraper import run

@pytest.mark.asyncio
async def test_facebook_run():
    result = await run("sofa")
    assert "success" in result
    assert "listings" in result
    assert isinstance(result["listings"], list)
