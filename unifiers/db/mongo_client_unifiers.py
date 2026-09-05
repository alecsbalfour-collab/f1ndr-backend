# f1ndr-backend/unifiers/db/mongo_client_unifiers.py
"""
Mongo client for Unifiers.
"""

from motor.motor_asyncio import AsyncIOMotorClient


def get_unifiers_client(uri: str):
    return AsyncIOMotorClient(uri)
