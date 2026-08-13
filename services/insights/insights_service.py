from engines.insights.insights_engine import InsightsEngine

class InsightsService:
    def __init__(self):
        self.engine = InsightsEngine()

    def process(self, payload):
        return self.engine.run(payload)
