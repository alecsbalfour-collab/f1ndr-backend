"""
Search Pipeline
Coordinates scraper → processor → unifier → trinn.
"""

from bs4 import BeautifulSoup
from trinn.module import trinn


class SearchPipeline:
    def __init__(self, scraper, processor, unifier):
        self.scraper = scraper
        self.processor = processor
        self.unifier = unifier

    def run(self, query: str, filters: dict, source: str):
        # 1. Fetch raw HTML
        raw_html = self.scraper.fetch_for_query(query, filters)
        if not raw_html:
            return []

        # 2. Parse HTML
        dom = BeautifulSoup(raw_html, "html.parser")

        # 3. Extract raw listings
        raw_listings = self.scraper.extract(dom)

        # 4. Unify listings
        unified = [self.unifier.unify(item, source) for item in raw_listings]

        # 5. Transform with trinn
        transformed = [trinn.transform(item) for item in unified]

        return transformed
