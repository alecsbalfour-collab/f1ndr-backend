from pymongo import MongoClient
from db.config.settings_db import load_db_settings


class DBClient:
    def __init__(self):
        settings = load_db_settings()
        host = settings.get("db_host", "localhost")
        port = int(settings.get("db_port", 27017))
        self.client = MongoClient(host=host, port=port)

    def connect(self):
        self.client.admin.command("ping")

    def disconnect(self):
        self.client.close()


def get_db_client():
    return DBClient()
