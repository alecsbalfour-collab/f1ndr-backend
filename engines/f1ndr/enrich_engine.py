class EnrichEngine:
    def enrich(self, listing: dict):
        return {
            **listing,
            "tags": self.generate_tags(listing),
            "fair_price": self.estimate_price(listing)
        }

    def generate_tags(self, listing: dict):
        tags = []
        title = listing.get("title", "").lower()
        desc = listing.get("description", "").lower()

        if "bike" in title or "bike" in desc:
            tags.append("bike")
        if "truck" in title:
            tags.append("vehicle")
        if "pet" in desc:
            tags.append("pet")

        return tags

    def estimate_price(self, listing: dict):
        price = listing.get("price")
        if price is None:
            return "unknown"
        return "fair"
