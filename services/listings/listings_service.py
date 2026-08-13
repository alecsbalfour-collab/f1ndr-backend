from engines.listings.listings_engine import ListingsEngine

class ListingsService:
    def __init__(self):
        self.engine = ListingsEngine()

    def process(self, payload):
        return self.engine.run(payload)
