from engines.f1ndr.f1ndr_engine import F1ndrEngine

class F1ndrController:
    def __init__(self):
        self.engine = F1ndrEngine()

    def search(self, query: str):
        return self.engine.run(query)
