from scrapers.scrapers.used_scraper import scrape_used

def test_used():
    result = scrape_used()
    assert "title" in result
    assert "url" in result
