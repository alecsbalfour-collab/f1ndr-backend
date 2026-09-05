# scrapers/db/scrapers_db_connection.py

import motor.motor_asyncio
import os

def get_scrapers_db():
    """
    Return MongoDB connection for scraper modules.
    """
    mongo_uri = os.getenv("F1NDR_MONGO_URI", "mongodb://localhost:27017")
    client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
    return client["f1ndr_scrapers"]
