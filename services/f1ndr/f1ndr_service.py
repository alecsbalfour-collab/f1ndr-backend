from engines.f1ndr.f1ndr_engine import F1ndrEngine

class F1ndrService:
    def __init__(self):
        self.engine = F1ndrEngine()

    def process(self, payload):
        return self.engine.run(payload)
