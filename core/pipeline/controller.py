from core.pipeline.state import PipelineState
from core.pipeline.router import PipelineRouter
from core.pipeline.events import PipelineEvents

class PipelineController:
    def __init__(self):
        self.state = PipelineState()
        self.router = PipelineRouter()
        self.events = PipelineEvents()

    def run(self, query: str, platforms: list[str] | None):
        self.state.reset()
        self.state.query = query
        self.state.platforms = platforms

        steps = self.router.get_steps()

        for step in steps:
            handler = self.router.get_handler(step)
            self.events.before_step(step, self.state)
            handler(self.state)
            self.events.after_step(step, self.state)

        return self.state.results
