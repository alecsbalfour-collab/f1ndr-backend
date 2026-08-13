from engines.search.search_engine import SearchEngine

class SearchService:
    def __init__(self):
        self.engine = SearchEngine()

    def process(self, payload):
        return self.engine.run(payload)
