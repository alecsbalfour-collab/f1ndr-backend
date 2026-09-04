from f1ndr.scrapers.kijiji_scraper import KijijiScraper
from f1ndr.processors.html_processor import HtmlProcessor
from f1ndr.unifiers.listing_unifier import ListingUnifier
from f1ndr.pipelines.search_pipeline import SearchPipeline

def test_search_pipeline():
    scraper = KijijiScraper()
    processor = HtmlProcessor()
    unifier = ListingUnifier()

    pipeline = SearchPipeline(scraper, processor, unifier)
    results = pipeline.run("bike", {}, "kijiji")

    assert isinstance(results, list)
