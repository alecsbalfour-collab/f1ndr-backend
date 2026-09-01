from services.f1ndr.listings_service import ListingsService

class ListingsController:
    """
    Controller for listing creation and posting.
    """

    def __init__(self):
        self.service = ListingsService()

    def create(self, listing):
        return self.service.create(listing)

    def push(self, listing):
        return self.service.push(listing)
