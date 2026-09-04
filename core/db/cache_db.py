# core/Db/cache_db.py

def get_cache() -> dict:
    """Minimal cache stub."""
    return {
        "connected": True,
        "driver": "internal-cache",
    }

def ping_cache(cache: dict) -> bool:
    """Simulate a cache ping."""
    return cache.get("connected", False)
