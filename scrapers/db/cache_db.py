# scrapers/db/cache_db.py

import asyncio

_cache_store = {}


async def cache_set(key: str, value: dict) -> None:
    """
    Store a value in the in-memory scraper cache.
    """
    _cache_store[key] = value


async def cache_get(key: str) -> dict | None:
    """
    Retrieve a cached value.
    """
    return _cache_store.get(key)


async def cache_delete(key: str) -> None:
    """
    Remove a cached value.
    """
    if key in _cache_store:
        del _cache_store[key]


async def cache_clear() -> None:
    """
    Clear all cached entries.
    """
    _cache_store.clear()
