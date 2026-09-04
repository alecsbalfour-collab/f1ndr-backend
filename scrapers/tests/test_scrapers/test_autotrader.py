from scrapers.scrapers.autotrader_scraper import scrape_autotrader

def test_autotrader():
    result = scrape_autotrader()
    assert "title" in result
    assert "url" in result
