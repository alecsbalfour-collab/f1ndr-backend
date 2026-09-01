from engines.f1ndr.f1ndr_engine import F1ndrEngine

class F1ndrService:
    def __init__(self):
        self.engine = F1ndrEngine()

    def search(self, query: str, platforms: list[str] | None):
        return self.engine.search(query, platforms)

    def create_listing(self, data):
        return self.engine.create_listing(data)

    def get_listings(self):
        return self.engine.get_listings()

    def clear_listings(self):
        return self.engine.clear_listings()
