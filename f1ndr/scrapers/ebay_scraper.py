class EbayScraper:
    def scrape(self, params: dict) -> dict:
        return {
            "platform": "ebay",
            "params": params,
            "status": "scraper_executed",
        }

ebay_scraper = EbayScraper()
