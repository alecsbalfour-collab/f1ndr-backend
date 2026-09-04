class ListingRepository:
    """
    Repository layer for indexing and searching listings in Elasticsearch.
    """

    def __init__(self, es_client):
        self.es = es_client

    def index(self, listing: dict):
        """
        Index a single listing into f1ndr.
        """
        self.es.index(index="f1ndr_listings", document=listing)

    def search(self, query: dict):
        """
        Perform a raw ES search query.
        """
        return self.es.search(index="f1ndr_listings", query=query)
