
from engines.f1ndr.scrapers_engine import ScrapersEngine

class ScrapersService:
    def __init__(self):
        self.engine = ScrapersEngine()

    def scrape(self, platforms: list, query: str):
        return self.engine.run_scrapers(platforms, query)
