class KnowledgeService:
    def __init__(self):
        self._store = {}

    def add(self, key, value):
        self._store[key] = value
        return {key: value}

    def get(self, key):
        return self._store.get(key)

    def all(self):
        return self._store
