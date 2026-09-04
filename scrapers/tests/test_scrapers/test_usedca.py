from scrapers.scrapers.usedca_scraper import scrape_usedca

def test_usedca():
    result = scrape_usedca()
    assert "title" in result
    assert "url" in result
