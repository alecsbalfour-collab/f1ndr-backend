from scrapers.scraper_manager import ScraperManager

class F1ndrEngine:
    def __init__(self):
        self.manager = ScraperManager()
        self.listings = []

    def search(self, query: str, platforms: list[str] | None):
        results = self.manager.run_scrapers(query, platforms)
        self.listings.extend(results)
        return results

    def create_listing(self, data):
        self.listings.append(data)
        return data

    def get_listings(self):
        return self.listings

    def clear_listings(self):
        self.listings = []
        return {"status": "cleared"}
