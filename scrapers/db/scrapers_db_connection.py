import os
from pymongo import MongoClient

class ScraperDBClient:
    """
    Wrapper so run_backend.py can call .connect() and .disconnect()
    without errors.
    """

    def __init__(self):
        host = os.getenv("SCRAPER_DB_HOST", "localhost")
        port = int(os.getenv("SCRAPER_DB_PORT", "27018"))
        self.client = MongoClient(host, port)

    def connect(self):
        # Force a real connection
        self.client.admin.command("ping")

    def disconnect(self):
        self.client.close()

def load_scraper_db_settings():
    return {
        "db_host": os.getenv("SCRAPER_DB_HOST", "localhost"),
        "db_port": int(os.getenv("SCRAPER_DB_PORT", "27018")),
        "db_name": os.getenv("SCRAPER_DB_NAME", "f1ndr_scraper"),
    }

def get_scraper_connection():
    settings = load_scraper_db_settings()
    client = MongoClient(settings["db_host"], settings["db_port"])
    return client[settings["db_name"]]

def get_scraper_db_client():
    return ScraperDBClient()

def ping_scraper_connection():
    try:
        ScraperDBClient().connect()
        return True
    except Exception:
        return False
