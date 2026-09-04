from scrapers.scrapers.rentfaster_scraper import scrape_rentfaster

def test_rentfaster():
    result = scrape_rentfaster()
    assert "title" in result
    assert "url" in result
