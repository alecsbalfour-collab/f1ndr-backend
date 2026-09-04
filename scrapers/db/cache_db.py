_cache = {}

def cache_listing(key: str, value: dict):
    _cache[key] = value

def get_cached_listing(key: str):
    return _cache.get(key)
