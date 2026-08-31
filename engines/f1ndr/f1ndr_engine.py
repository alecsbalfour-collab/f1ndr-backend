from engines.f1ndr.search_engine import SearchEngine
from engines.f1ndr.platforms_engine import PlatformsEngine
from engines.f1ndr.scrapers_engine import ScrapersEngine
from engines.f1ndr.normalize_engine import NormalizeEngine
from engines.f1ndr.dedupe_engine import DedupeEngine
from engines.f1ndr.enrich_engine import EnrichEngine
from engines.f1ndr.listings_engine import ListingsEngine
from engines.f1ndr.index_engine import IndexEngine


class F1ndrEngine:
    def __init__(self):
        self.search = SearchEngine()
        self.platforms = PlatformsEngine()
        self.scrapers = ScrapersEngine()
        self.normalize = NormalizeEngine()
        self.dedupe = DedupeEngine()
        self.enrich = EnrichEngine()
        self.listings = ListingsEngine()
        self.index = IndexEngine()

    def run(self, query: str):
        # 1. classify query
        category = self.search.classify(query)

        # 2. choose platforms
        platforms = self.platforms.get_platforms(category)

        # 3. scrape raw listings
        raw_results = self.scrapers.run_scrapers(platforms, query)

        # 4. normalize
        normalized = [self.normalize.normalize(item) for item in raw_results]

        # 5. dedupe
        deduped = self.dedupe.dedupe(normalized)

        # 6. enrich
        enriched = [self.enrich.enrich(item) for item in deduped]

        # 7. format listings
        formatted = [self.listings.format(item) for item in enriched]

        # 8. index
        for item in formatted:
            self.index.push(item)

        return {
            "query": query,
            "category": category,
            "platforms_used": platforms,
            "total_results": len(formatted),
            "results": formatted
        }
