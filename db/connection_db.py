# db/connection_db.py
# Enterprise MongoDB connection layer for F1NDR

from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
import os

client: AsyncIOMotorClient | None = None
db = None


def get_database():
    return db


async def connect_to_db(app: FastAPI):
    global client, db

    mongo_uri = os.getenv("MONGO_URI")
    mongo_db = os.getenv("MONGO_DB", "f1ndr")

    if not mongo_uri:
        raise RuntimeError("MONGO_URI environment variable is missing.")

    client = AsyncIOMotorClient(mongo_uri)
    db = client[mongo_db]

    app.state.db = db
    print("📡 Connected to MongoDB Atlas")


async def close_db_connection(app: FastAPI):
    global client

    if client:
        client.close()
        print("🔌 MongoDB connection closed")
