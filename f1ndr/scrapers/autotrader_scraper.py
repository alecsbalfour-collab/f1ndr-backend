class AutotraderScraper:
    def scrape(self, params: dict) -> dict:
        return {
            "platform": "autotrader",
            "params": params,
            "status": "scraper_executed",
        }

autotrader_scraper = AutotraderScraper()
