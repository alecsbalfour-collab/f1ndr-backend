from engines.scrapers.scrapers_engine import ScrapersEngine

class ScrapersService:
    def __init__(self):
        self.engine = ScrapersEngine()

    def process(self, payload):
        return self.engine.run(payload)
