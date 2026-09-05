class ListingUnifier:
    def unify(self, listing: dict) -> dict:
        return {
            "listing": listing,
            "status": "listing_unifier_executed",
        }

listing_unifier = ListingUnifier()
