# utils/db/cache.py

class UtilsCache:
    """
    Lightweight global cache for backend utilities.
    """
    def __init__(self):
        self._store = {}

    def get(self, key):
        return self._store.get(key)

    def set(self, key, value):
        self._store[key] = value

    def clear(self):
        self._store.clear()

utils_cache = UtilsCache()
