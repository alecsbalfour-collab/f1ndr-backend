from scrapers.scraper_manager import ScraperManager

class ScrapersEngine:
    def __init__(self):
        self.manager = ScraperManager()

    def run(self, query: str, platforms: list[str]):
        results = []
        for p in platforms:
            try:
                results.extend(self.manager.run(query, p))
            except Exception:
                continue
        return results
