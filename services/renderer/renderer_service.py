from engines.renderer.renderer_engine import RendererEngine

class RendererService:
    def __init__(self):
        self.engine = RendererEngine()

    def process(self, payload):
        return self.engine.run(payload)
