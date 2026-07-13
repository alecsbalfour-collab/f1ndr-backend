class RegistryService:
    """
    Simple key/value registry used by WCHTR renderer and voice services.
    """

    def __init__(self):
        self._store = {}

    def set(self, key: str, value):
        self._store[key] = value
        return value

    def get(self, key: str):
        return self._store.get(key)

    def all(self):
        return dict(self._store)

    def delete(self, key: str):
        if key in self._store:
            del self._store[key]
            return True
        return False
