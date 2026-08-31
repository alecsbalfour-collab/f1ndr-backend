class ListingsEngine:
    def __init__(self):
        self.state = {
            "listings": [],
            "filters": {},
            "results": [],
            "log": []
        }

    def add_listing(self, listing: dict):
        self.state["listings"].append(listing)
        self.state["log"].append(f"Added listing: {listing.get('title', 'unknown')}")

    def apply_filters(self, filters: dict):
        self.state["filters"] = filters
        self.state["log"].append(f"Applied filters: {filters}")

        results = self.state["listings"]

        if "platform" in filters:
            results = [
                l for l in results
                if l.get("platform", "").lower() == filters["platform"].lower()
            ]

        if "min_price" in filters:
            results = [
                l for l in results
                if l.get("price", 0) >= filters["min_price"]
            ]

        if "max_price" in filters:
            results = [
                l for l in results
                if l.get("price", 0) <= filters["max_price"]
            ]

        if "condition" in filters:
            results = [
                l for l in results
                if l.get("condition", "").lower() == filters["condition"].lower()
            ]

        self.state["results"] = results
        self.state["log"].append(f"Filtered down to {len(results)} listings")

    def score_listings(self):
        scored = []

        for listing in self.state["results"]:
            price = listing.get("price", 0)
            condition = listing.get("condition", "unknown")

            score = 100

            if price > 1000:
                score -= 20
            if condition.lower() == "poor":
                score -= 30
            if condition.lower() == "excellent":
                score += 10

            listing["score"] = score
            scored.append(listing)

        self.state["results"] = scored
        self.state["log"].append("Scored listings")

    def snapshot(self):
        return self.state
