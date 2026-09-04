from scrapers.scrapers.realtor_scraper import scrape_realtor

def test_realtor():
    result = scrape_realtor()
    assert "title" in result
    assert "url" in result
