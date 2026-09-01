from scrapers.kijiji_scraper import KijijiScraper
from scrapers.facebook_scraper import FacebookScraper
from scrapers.autotrader_scraper import AutotraderScraper
from scrapers.craigslist_scraper import CraigslistScraper
from scrapers.usedca_scraper import UsedCaScraper
from scrapers.marketplace_scraper import MarketplaceCaScraper
from scrapers.ebay_scraper import EbayScraper
from scrapers.realtor_scraper import RealtorScraper
from scrapers.rentfaster_scraper import RentfasterScraper
from scrapers.zillow_scraper import ZillowScraper

class ScraperManager:
    def __init__(self):
        self.scrapers = {
            "kijiji": KijijiScraper(),
            "facebook": FacebookScraper(),
            "autotrader": AutotraderScraper(),
            "craigslist": CraigslistScraper(),
            "usedca": UsedCaScraper(),
            "marketplace_ca": MarketplaceCaScraper(),
            "ebay": EbayScraper(),
            "realtor": RealtorScraper(),
            "rentfaster": RentfasterScraper(),
            "zillow": ZillowScraper(),
        }

    def run(self, query: str, platform: str):
        scraper = self.scrapers.get(platform)
        if scraper:
            return scraper.scrape(query)
        return []
