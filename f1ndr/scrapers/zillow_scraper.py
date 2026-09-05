class ZillowScraper:
    def scrape(self, params: dict) -> dict:
        return {
            "platform": "zillow",
            "params": params,
            "status": "scraper_executed",
        }

zillow_scraper = ZillowScraper()
