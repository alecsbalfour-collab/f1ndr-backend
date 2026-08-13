class ListingsEngine:
    def normalize(self, item):
        return {
            "title": item.get("title", "").strip(),
            "price": float(item.get("price", 0)),
            "platform": item.get("platform", ""),
            "url": item.get("url", ""),
            "posted": item.get("posted", ""),
            "location": item.get("location", ""),
            "condition": item.get("condition", "unknown"),
            "distance_km": item.get("distance_km", None)
        }

    def dedupe(self, items):
        seen = set()
        unique = []
        for item in items:
            key = (item["title"], item["price"], item["platform"])
            if key not in seen:
                seen.add(key)
                unique.append(item)
        return unique

    def distance_score(self, km):
        if km is None:
            return 0
        if km < 5: return 20
        if km < 10: return 15
        if km < 20: return 10
        if km < 40: return 5
        return 0

    def score(self, item):
        price = item["price"]
        condition = item["condition"].lower()
        title = item["title"].lower()
        km = item.get("distance_km", None)

        score = 50

        if price < 150: score += 25
        elif price < 300: score += 15
        elif price < 500: score += 10
        else: score += 5

        if "new" in condition: score += 15
        if "like new" in condition: score += 10
        if "used" in condition: score += 5

        keywords = ["rare", "mint", "upgraded", "custom"]
        for k in keywords:
            if k in title:
                score += 5

        score += self.distance_score(km)

        return score

    def run(self, payload):
        raw_items = payload.get("items", [])
        normalized = [self.normalize(i) for i in raw_items]
        deduped = self.dedupe(normalized)

        for item in deduped:
            item["deal_score"] = self.score(item)

        sorted_items = sorted(deduped, key=lambda x: x["deal_score"], reverse=True)

        return {
            "count": len(sorted_items),
            "results": sorted_items
        }
