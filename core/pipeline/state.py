class PipelineState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.query = None
        self.platforms = None
        self.raw_results = []
        self.normalized = []
        self.deduped = []
        self.enriched = []
        self.indexed = []
        self.results = []
