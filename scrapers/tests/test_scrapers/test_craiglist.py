from scrapers.scrapers.craigslist_scraper import scrape_craigslist

def test_craigslist():
    result = scrape_craigslist()
    assert "title" in result
    assert "url" in result
