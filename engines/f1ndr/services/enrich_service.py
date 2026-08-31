from engines.f1ndr.enrich_engine import EnrichEngine

class EnrichService:
    def __init__(self):
        self.engine = EnrichEngine()

    def enrich_all(self, items: list):
        return [self.engine.enrich(item) for item in items]
