from services.f1ndr.search_service import SearchService

class SearchController:
    """
    Controller for search operations.
    """

    def __init__(self):
        self.service = SearchService()

    def run(self, query: str, platforms: list[str] | None):
        return self.service.run(query, platforms)
