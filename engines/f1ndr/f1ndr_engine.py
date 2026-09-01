from engines.f1ndr.search_engine import SearchEngine
from engines.f1ndr.platforms_engine import PlatformsEngine
from engines.f1ndr.scrapers_engine import ScrapersEngine
from engines.f1ndr.normalize_engine import NormalizeEngine
from engines.f1ndr.dedupe_engine import DedupeEngine
from engines.f1ndr.rank_engine import RankEngine
from engines.f1ndr.enrich_engine import EnrichEngine
from engines.f1ndr.index_engine import IndexEngine

class F1ndrEngine:
    def __init__(self):
        self.search_engine = SearchEngine()
        self.platforms_engine = PlatformsEngine()
        self.scrapers_engine = ScrapersEngine()
        self.normalize_engine = NormalizeEngine()
        self.dedupe_engine = DedupeEngine()
        self.rank_engine = RankEngine()
        self.enrich_engine = EnrichEngine()
        self.index_engine = IndexEngine()

    def run(self, query: str, platforms=None):
        search_data = self.search_engine.run(query)
        selected_platforms = self.platforms_engine.run(platforms)
        listings = self.scrapers_engine.run(search_data["query"], selected_platforms)
        listings = self.normalize_engine.run(listings)
        listings = self.dedupe_engine.run(listings)
        listings = self.enrich_engine.run(listings)
        listings = self.rank_engine.run(listings)
        listings = self.index_engine.run(listings)
        return listings
