import pytest
from scrapers.scrapers.autotrader_scraper import run

@pytest.mark.asyncio
async def test_autotrader_run():
    result = await run("car")
    assert "success" in result
    assert isinstance(result["listings"], list)
