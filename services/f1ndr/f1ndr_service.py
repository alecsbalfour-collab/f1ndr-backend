from engines.f1ndr_engine import F1ndrEngine

class F1ndrService:
    def __init__(self):
        self.engine = F1ndrEngine()

    def run(self, payload):
        # Non-logic: just pass through
        return self.engine.run(payload)
