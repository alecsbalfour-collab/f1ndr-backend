from engines.f1ndr.listings_engine import ListingsEngine

class ListingsService:
    def __init__(self):
        self.engine = ListingsEngine()

    def format_all(self, items: list):
        return [self.engine.format(item) for item in items]
