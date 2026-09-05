# scrapers/db/queue_db.py

import asyncio

_scraper_queue = []


async def queue_push(item: dict) -> None:
    """
    Push an item into the scraper queue.
    """
    _scraper_queue.append(item)


async def queue_pop() -> dict | None:
    """
    Pop the next item from the scraper queue.
    """
    if _scraper_queue:
        return _scraper_queue.pop(0)
    return None


async def queue_size() -> int:
    """
    Return the number of items in the queue.
    """
    return len(_scraper_queue)


async def queue_clear() -> None:
    """
    Clear the queue.
    """
    _scraper_queue.clear()
