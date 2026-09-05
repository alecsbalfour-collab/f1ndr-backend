class PipelineState:
    def __init__(self):
        self.runs = 0

    def increment_runs(self):
        self.runs += 1


pipeline_state = PipelineState()
