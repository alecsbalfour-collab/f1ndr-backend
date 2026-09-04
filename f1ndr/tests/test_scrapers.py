from f1ndr.scrapers.kijiji_scraper import KijijiScraper

def test_kijiji_scraper_fetch():
    scraper = KijijiScraper()
    html = scraper.fetch_for_query("bike", {})
    assert isinstance(html, str)

def test_kijiji_scraper_extract():
    scraper = KijijiScraper()
    sample_html = "<div class='search-item'><a href='/v-bike'>Bike</a><div class='price'>$100</div></div>"
    dom = scraper.parse(sample_html)
    listings = scraper.extract(dom)
    assert len(listings) >= 1
    assert listings[0]["title"] == "Bike"
