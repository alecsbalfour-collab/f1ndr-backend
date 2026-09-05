def test_autotrader_scraper():
    from f1ndr.scrapers import autotrader_scraper
    result = autotrader_scraper.scrape({"q": "cars"})
    assert result["status"] == "scraper_executed"


def test_kijiji_scraper():
    from f1ndr.scrapers import kijiji_scraper
    result = kijiji_scraper.scrape({"q": "rentals"})
    assert result["status"] == "scraper_executed"


def test_zillow_scraper():
    from f1ndr.scrapers import zillow_scraper
    result = zillow_scraper.scrape({"q": "homes"})
    assert result["status"] == "scraper_executed"
