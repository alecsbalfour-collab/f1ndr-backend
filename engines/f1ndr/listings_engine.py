class ListingsEngine:
    def format(self, listing: dict):
        return {
            "id": listing["id"],
            "title": listing["title"],
            "price": listing["price"],
            "location": listing["location"],
            "tags": listing.get("tags", []),
            "url": listing["url"]
        }
