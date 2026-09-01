class RankEngine:
    def run(self, listings):
        return sorted(listings, key=lambda x: x["price"])
