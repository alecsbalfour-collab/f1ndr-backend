from engines.f1ndr.index_engine import IndexEngine

class IndexService:
    def __init__(self):
        self.engine = IndexEngine()

    def add(self, item: dict):
        self.engine.push(item)

    def search(self, query: str):
        return self.engine.search(query)
