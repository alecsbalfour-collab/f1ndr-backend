from engines.f1ndr.f1ndr_engine import F1ndrEngine
from engines.f1ndr.core.f1ndr_controller import F1ndrController
from engines.f1ndr.core.f1ndr_pipeline import F1ndrPipeline
from engines.f1ndr.core.f1ndr_router import F1ndrRouter

class F1ndr:
    def __init__(self):
        self.engine = F1ndrEngine()
        self.controller = F1ndrController()
        self.pipeline = F1ndrPipeline()
        self.router = F1ndrRouter()

    def search(self, query: str):
        return self.controller.search(query)

    def run(self, query: str):
        return self.engine.run(query)

    def handle(self, payload: dict):
        return self.router.handle(payload)

# Singleton-style instance
f1ndr = F1ndr()
