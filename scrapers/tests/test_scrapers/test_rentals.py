from scrapers.scrapers.rentals_scraper import scrape_rentals

def test_rentals():
    result = scrape_rentals()
    assert "title" in result
    assert "url" in result
