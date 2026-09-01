from engines.f1ndr.search_engine import SearchEngine
from engines.f1ndr.platforms_engine import PlatformsEngine
from engines.f1ndr.scrapers_engine import ScrapersEngine
from engines.f1ndr.normalize_engine import NormalizeEngine
from engines.f1ndr.dedupe_engine import DedupeEngine
from engines.f1ndr.rank_engine import RankEngine


class F1ndrEngine:
    def __init__(self):
        self.search_engine = SearchEngine()
        self.platforms_engine = PlatformsEngine()
        self.scrapers_engine = ScrapersEngine()
        self.normalize_engine = NormalizeEngine()
        self.dedupe_engine = DedupeEngine()
        self.rank_engine = RankEngine()

    def run(self, query: str, platforms: list[str] | None = None):
        # 1. Search interpretation
        search_data = self.search_engine.run(query)

        # 2. Platform selection
        selected_platforms = self.platforms_engine.run(platforms)

        # 3. Scrape raw listings
        raw_listings = self.scrapers_engine.run(search_data["query"], selected_platforms)

        # 4. Normalize
        normalized = self.normalize_engine.run(raw_listings)

        # 5. Dedupe
        deduped = self.dedupe_engine.run(normalized)

        # 6. Rank
        ranked = self.rank_engine.run(deduped)

        return ranked
