class SearchEngine:
    def classify(self, query: str):
        query = query.lower()

        if any(x in query for x in ["bike", "bicycle", "mtb"]):
            return "bikes"
        if any(x in query for x in ["truck", "car", "vehicle"]):
            return "vehicles"
        if any(x in query for x in ["dog", "cat", "pet"]):
            return "pets"

        return "general"
