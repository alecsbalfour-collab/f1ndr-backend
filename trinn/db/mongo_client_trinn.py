# f1ndr-backend/trinn/db/mongo_client_trinn.py
"""
Mongo client for TRINN.
"""

from motor.motor_asyncio import AsyncIOMotorClient


def get_trinn_client(uri: str):
    return AsyncIOMotorClient(uri)
