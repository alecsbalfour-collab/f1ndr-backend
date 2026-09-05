class UsedScraper:
    def scrape(self, params: dict) -> dict:
        return {
            "platform": "used",
            "params": params,
            "status": "scraper_executed",
        }

used_scraper = UsedScraper()
