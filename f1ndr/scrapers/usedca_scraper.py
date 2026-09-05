class UsedCAScraper:
    def scrape(self, params: dict) -> dict:
        return {
            "platform": "usedca",
            "params": params,
            "status": "scraper_executed",
        }

usedca_scraper = UsedCAScraper()
