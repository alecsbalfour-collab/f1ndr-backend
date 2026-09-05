class MongoClientDB:
    def __init__(self, uri: str = "mongodb://localhost:27017", database: str = "listr"):
        self.uri = uri
        self.database = database

    def info(self) -> dict:
        return {
            "uri": self.uri,
            "database": self.database,
        }


mongo_client_db = MongoClientDB()
