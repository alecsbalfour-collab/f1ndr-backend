class ListingsService:
    """
    Listing creation, editing, and posting.
    """

    def create(self, listing):
        return {
            "status": "created",
            "id": "listing_123",
            "payload": listing.dict()
        }

    def push(self, listing):
        return {
            "status": "pushed",
            "platforms": ["kijiji", "facebook"]
        }
