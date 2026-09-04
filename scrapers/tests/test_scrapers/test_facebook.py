from scrapers.scrapers.facebook_scraper import scrape_facebook

def test_facebook():
    result = scrape_facebook()
    assert "title" in result
    assert "url" in result
