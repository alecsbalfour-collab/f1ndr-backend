class DBConnection:
    def __init__(self, host="localhost", port=27017, database="f1ndr"):
        self.host = host
        self.port = port
        self.database = database

    def info(self) -> dict:
        return {
            "host": self.host,
            "port": self.port,
            "database": self.database,
        }

db_connection = DBConnection()
