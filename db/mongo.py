from pymongo import MongoClient
import os

# Environment variables or defaults
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "watchr")

client = MongoClient(MONGO_URL)
db = client[DB_NAME]


def get_listings_collection():
    return db["listings"]


def get_platforms_collection():
    return db["platforms"]


def get_discovery_collection():
    return db["discovered_sites"]
3