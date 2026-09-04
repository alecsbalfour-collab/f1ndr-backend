from scrapers.scrapers.ebay_scraper import scrape_ebay

def test_ebay():
    result = scrape_ebay()
    assert "title" in result
    assert "url" in result
