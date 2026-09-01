from core.config.constants import PIPELINE_STEPS
from core.utils.errors import PipelineError

class PipelineRouter:
    def __init__(self):
        self.handlers = {}

    def register(self, step_name: str, handler):
        self.handlers[step_name] = handler

    def get_steps(self):
        return PIPELINE_STEPS

    def get_handler(self, step_name: str):
        if step_name not in self.handlers:
            raise PipelineError(f"No handler registered for step: {step_name}")
        return self.handlers[step_name]
