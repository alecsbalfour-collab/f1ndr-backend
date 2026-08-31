class IndexEngine:
    def __init__(self):
        self.index = []

    def push(self, listing: dict):
        self.index.append(listing)

    def search(self, query: str):
        q = query.lower()
        return [
            item for item in self.index
            if q in item.get("title", "").lower()
        ]
