from engines.search.search_engine import SearchEngine
from engines.platforms.platforms_engine import PlatformsEngine
from engines.scrapers.scrapers_engine import ScrapersEngine
from engines.listings.listings_engine import ListingsEngine

class F1ndrEngine:
    def __init__(self):
        self.search = SearchEngine()
        self.platforms = PlatformsEngine()
        self.scrapers = ScrapersEngine()
        self.listings = ListingsEngine()

    def run(self, payload):
        search_result = self.search.run({"query": payload.get("query", "")})
        category = search_result["category"]
        platforms = search_result["platforms"]

        enabled_platforms = self.platforms.get_enabled()
        category_platforms = self.platforms.filter_by_category(category)

        final_platforms = [
            p for p in platforms
            if p in enabled_platforms and p in category_platforms
        ]

        scraped = self.scrapers.run({
            "query": search_result["query"],
            "platforms": final_platforms
        })

        aggregated = self.listings.run({"items": scraped["results"]})

        return {
            "query": search_result["query"],
            "category": category,
            "platforms_used": final_platforms,
            "total_results": aggregated["count"],
            "results": aggregated["results"]
        }
