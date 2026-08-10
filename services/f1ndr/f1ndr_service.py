import re

class F1ndrService:
    def __init__(self):
        self._cache = {}

    # ---------------------------------------------------------
    # PLATFORM DETECTION
    # ---------------------------------------------------------
    def _detect_platform(self, target: str):
        target = target.lower()

        patterns = {
            "kijiji": r"kijiji",
            "facebook": r"facebook|fb\.com|fb\.me",
            "craigslist": r"craigslist",
            "ebay": r"ebay",
            "marketplace": r"marketplace"
        }

        for platform, pattern in patterns.items():
            if re.search(pattern, target):
                return platform

        return None

    # ---------------------------------------------------------
    # SCRAPER LOADER
    # ---------------------------------------------------------
    def _load_scraper(self, platform: str):
        try:
            module = __import__(f"scrapers.{platform}", fromlist=["scrape"])
            return module.scrape
        except Exception as e:
            return None

    # ---------------------------------------------------------
    # LISTING NORMALIZER
    # ---------------------------------------------------------
    def _normalize(self, raw: dict, platform: str, target: str):
        return {
            "title": raw.get("title", "Untitled"),
            "price": raw.get("price", "N/A"),
            "url": target,
            "location": raw.get("location", "Unknown"),
            "source": platform,
            "raw": raw
        }

    # ---------------------------------------------------------
    # SEARCH
    # ---------------------------------------------------------
    def search(self, payload: dict):
        query = payload.get("query")
        if not query:
            return {"error": "Missing 'query' field"}

        return {
            "action": "search",
            "query": query,
            "results": ["result_1", "result_2"]
        }

    # ---------------------------------------------------------
    # SCRAPE
    # ---------------------------------------------------------
    def scrape(self, payload: dict):
        target = payload.get("target")
        if not target:
            return {"error": "Missing 'target' field"}

        # Detect platform
        platform = self._detect_platform(target)
        if not platform:
            return {
                "error": "Unknown platform",
                "target": target
            }

        # Load scraper
        scraper = self._load_scraper(platform)
        if not scraper:
            return {
                "error": f"Scraper for '{platform}' could not be loaded."
            }

        # Run scraper
        try:
            raw = scraper(target)
        except Exception as e:
            return {"error": f"Scraper error: {e}"}

        # Normalize
        normalized = self._normalize(raw, platform, target)

        return {
            "action": "scrape",
            "platform": platform,
            "target": target,
            "result": normalized
        }

    # ---------------------------------------------------------
    # RENDER
    # ---------------------------------------------------------
    def render(self, payload: dict):
        data = payload.get("data")
        if not data:
            return {"error": "Missing 'data' field"}

        return {
            "action": "render",
            "input": data,
            "frame": "rendered-frame"
        }

    # ---------------------------------------------------------
    # CONTRACT
    # ---------------------------------------------------------
    def contract(self, payload: dict):
        text = payload.get("text")
        if not text:
            return {"error": "Missing 'text' field"}

        return {
            "action": "contract",
            "input": text,
            "output": f"contract-output-for: {text}"
        }
