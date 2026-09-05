class KijijiScraper:
    def scrape(self, params: dict) -> dict:
        return {
            "platform": "kijiji",
            "params": params,
            "status": "scraper_executed",
        }

kijiji_scraper = KijijiScraper()
