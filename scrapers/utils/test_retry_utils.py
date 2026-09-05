import pytest
import asyncio
from scrapers.utils.retry_utils import retry

@pytest.mark.asyncio
async def test_retry_success():
    calls = {"count": 0}

    @retry(attempts=3)
    async def sample():
        calls["count"] += 1
        return "ok"

    result = await sample()
    assert result == "ok"
    assert calls["count"] == 1
