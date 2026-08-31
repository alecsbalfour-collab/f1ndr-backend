from engines.f1ndr.search_engine import SearchEngine

class SearchService:
    def __init__(self):
        self.engine = SearchEngine()

    def classify(self, query: str):
        return self.engine.classify(query)
