from scrapers.scrapers.zillow_scraper import scrape_zillow

def test_zillow():
    result = scrape_zillow()
    assert "title" in result
    assert "url" in result
