from scrapers.scrapers.kijiji_scraper import scrape_kijiji

def test_kijiji():
    result = scrape_kijiji()
    assert "title" in result
    assert "url" in result
