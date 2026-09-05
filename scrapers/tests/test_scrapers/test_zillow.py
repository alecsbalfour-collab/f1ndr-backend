import pytest
from scrapers.scrapers.zillow_scraper import run

@pytest.mark.asyncio
async def test_zillow_run():
    result = await run("rent")
    assert "success" in result
    assert isinstance(result["listings"], list)
