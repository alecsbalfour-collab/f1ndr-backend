# f1ndr_backend/db/indexing.py

from motor.motor_asyncio import AsyncIOMotorDatabase

async def apply_indexes(db: AsyncIOMotorDatabase):
    """
    Apply all MongoDB indexes for F1NDR collections.
    """

    # Listings collection
    await db.listings.create_index("listing_id", unique=True)
    await db.listings.create_index("vin")
    await db.listings.create_index([("price", 1)])
    await db.listings.create_index([("created_at", -1)])

    # Dealers collection
    await db.dealers.create_index("dealer_id", unique=True)
    await db.dealers.create_index([("location.coordinates", "2dsphere")])

    # Ingestion history
    await db.ingestion_history.create_index("source")
    await db.ingestion_history.create_index([("timestamp", -1)])
