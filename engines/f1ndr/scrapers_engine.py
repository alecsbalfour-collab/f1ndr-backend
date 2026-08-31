class ScrapersEngine:
    def run_scrapers(self, platforms: list, query: str):
        results = []

        for platform in platforms:
            results.append({
                "id": f"{platform}-123",
                "title": f"{query} listing from {platform}",
                "price": 100,
                "location": "Calgary",
                "description": f"Sample {query} listing from {platform}",
                "images": [],
                "platform": platform,
                "url": f"https://{platform}.com/listing/123",
                "posted": "2026-08-31"
            })

        return results
