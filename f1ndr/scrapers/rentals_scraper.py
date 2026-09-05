class RentalsScraper:
    def scrape(self, params: dict) -> dict:
        return {
            "platform": "rentals",
            "params": params,
            "status": "scraper_executed",
        }

rentals_scraper = RentalsScraper()
