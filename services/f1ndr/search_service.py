from engines.f1ndr.f1ndr import f1ndr

class SearchService:
    """
    Dedicated search service.
    """

    def run(self, query: str, platforms: list[str] | None):
        return f1ndr.search(query, platforms)
