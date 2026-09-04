"""
f1ndr service layer.
Handles orchestration: scrapers → processors → engines → unifiers → trinn.
"""

from f1ndr.scrapers.kijiji_scraper import KijijiScraper
# later: import other scrapers (facebook, craigslist, etc.)

from f1ndr.engines.html_engine import HtmlEngine
from f1ndr.processors.html_processor import HtmlProcessor
from f1ndr.unifiers.listing_unifier import ListingUnifier

from trinn.module import trinn  # dict-based normalize/transform/enrich


class F1ndrService:
    def __init__(self):
        self.kijiji_scraper = KijijiScraper()
        self.html_engine = HtmlEngine()
        self.html_processor = HtmlProcessor()
        self.unifier = ListingUnifier()

    def search(self, payload: dict):
        query = payload.get("query", "")
        sources = payload.get("sources", ["kijiji"])
        filters = payload.get("filters", {})

        results = []

        if "kijiji" in sources:
            raw_html = self.kijiji_scraper.fetch_for_query(query, filters)
            dom = self.html_engine.parse(raw_html)
            raw_listings = self.html_processor.extract_listings(dom)
            unified = [self.unifier.unify(l, source="kijiji") for l in raw_listings]
            transformed = [trinn.transform(item) for item in unified]
            results.extend(transformed)

        return {
            "query": query,
            "sources": sources,
            "results": results,
        }
