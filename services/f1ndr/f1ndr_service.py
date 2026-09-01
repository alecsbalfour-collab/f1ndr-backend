from engines.f1ndr.f1ndr import f1ndr

class F1ndrService:
    """
    High-level service that exposes the f1ndr engine pipeline.
    """

    def search(self, query: str, platforms: list[str] | None):
        return f1ndr.search(query, platforms)

    def create_listing(self, data):
        # Placeholder until listing creation logic is added
        return {
            "status": "created",
            "id": "listing_123",
            "data": data.dict()
        }

    def push_listing(self, data):
        # Placeholder until platform posting logic is added
        return {
            "status": "pushed",
            "platforms": ["kijiji", "facebook"]
        }
