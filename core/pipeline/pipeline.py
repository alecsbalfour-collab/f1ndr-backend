from core.pipeline.controller import PipelineController

class Pipeline:
    def __init__(self):
        self.controller = PipelineController()

    def run(self, query: str, platforms: list[str] | None):
        return self.controller.run(query, platforms)
