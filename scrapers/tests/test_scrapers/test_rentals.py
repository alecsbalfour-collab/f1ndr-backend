import pytest
import asyncio
from scrapers.scrapers.rentals_scraper import run

@pytest.mark.asyncio
async def test_rentals_run():
    result = await run("apartment")
    assert "success" in result
    assert "listings" in result
    assert isinstance(result["listings"], list)
