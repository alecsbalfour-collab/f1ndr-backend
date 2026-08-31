from engines.f1ndr.dedupe_engine import DedupeEngine

class DedupeService:
    def __init__(self):
        self.engine = DedupeEngine()

    def dedupe(self, items: list):
        return self.engine.dedupe(items)
