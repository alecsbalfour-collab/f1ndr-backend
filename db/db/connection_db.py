from pymongo import MongoClient
from db.config.settings_db import load_db_settings


def get_db_client():
    """
    Returns a MongoDB client using settings loaded from settings_db.py.
    This matches how run_backend.py calls the function (no arguments).
    """
    settings = load_db_settings()

    host = settings.get("db_host", "localhost")
    port = int(settings.get("db_port", 27017))

    return MongoClient(host=host, port=port)
