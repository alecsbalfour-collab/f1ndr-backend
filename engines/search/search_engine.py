class SearchEngine:
    def normalize(self, query: str):
        return query.strip().lower()

    def expand(self, query: str):
        synonyms = {
            "bike": ["bicycle", "mtb", "mountain bike"],
            "car": ["vehicle", "auto"]
        }
        expanded = []
        for word in query.split():
            expanded.extend(synonyms.get(word, []))
        return expanded

    def classify(self, query: str):
        if "bike" in query or "mtb" in query:
            return "bicycles"
        if "car" in query:
            return "vehicles"
        return "general"

    def route_platforms(self, category: str):
        mapping = {
            "bicycles": ["kijiji", "facebook", "craigslist"],
            "vehicles": ["kijiji", "autotrader"]
        }
        return mapping.get(category, ["kijiji"])

    def run(self, payload):
        query = payload.get("query", "")
        normalized = self.normalize(query)
        expanded = self.expand(normalized)
        category = self.classify(normalized)
        platforms = self.route_platforms(category)

        return {
            "query": normalized,
            "expanded_terms": expanded,
            "category": category,
            "platforms": platforms
        }
