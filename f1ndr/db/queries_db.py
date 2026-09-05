class DBQueries:
    def find(self, collection: str, query: dict) -> dict:
        return {
            "collection": collection,
            "query": query,
        }

    def insert(self, collection: str, document: dict) -> dict:
        return {
            "collection": collection,
            "inserted": document,
        }

    def update(self, collection: str, query: dict, update: dict) -> dict:
        return {
            "collection": collection,
            "query": query,
            "update": update,
        }

db_queries = DBQueries()
