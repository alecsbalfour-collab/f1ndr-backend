from scrapers.scrapers.marketplace_scraper import scrape_marketplace

def test_marketplace():
    result = scrape_marketplace()
    assert "title" in result
    assert "url" in result
