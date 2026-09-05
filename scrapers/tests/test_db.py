# scrapers/tests/test_db.py

import pytest
import asyncio

from scrapers.db.cache_db import cache_set, cache_get, cache_delete, cache_clear
from scrapers.db.queue_db import queue_push, queue_pop, queue_size, queue_clear
from scrapers.db.scrapers_db_connection import get_scrapers_db


@pytest.mark.asyncio
async def test_cache_db():
    await cache_clear()
    await cache_set("key", {"value": 1})
    assert await cache_get("key") == {"value": 1}
    await cache_delete("key")
    assert await cache_get("key") is None


@pytest.mark.asyncio
async def test_queue_db():
    await queue_clear()
    await queue_push({"item": 1})
    assert await queue_size() == 1
    popped = await queue_pop()
    assert popped == {"item": 1}
    assert await queue_size() == 0


def test_scrapers_db_connection():
    db = get_scrapers_db()
    assert db is not None
