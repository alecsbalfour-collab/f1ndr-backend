# config/db/cache.py

class ConfigCache:
    """
    Global configuration cache.
    Stores resolved config sections for fast access.
    """
    def __init__(self):
        self._store = {}

    def get(self, section):
        return self._store.get(section)

    def set(self, section, value):
        self._store[section] = value

config_cache = ConfigCache()
