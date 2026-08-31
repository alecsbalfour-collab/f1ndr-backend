from engines.f1ndr.normalize_engine import NormalizeEngine

class NormalizeService:
    def __init__(self):
        self.engine = NormalizeEngine()

    def normalize_all(self, items: list):
        return [self.engine.normalize(item) for item in items]
