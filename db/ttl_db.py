# f1ndr_backend/db/ttl.py

from motor.motor_asyncio import AsyncIOMotorDatabase

async def apply_ttl(db: AsyncIOMotorDatabase):
    """
    Apply TTL indexes for auto-expiring collections.
    """

    # Ingestion temp data expires after 24 hours
    await db.ingestion_temp.create_index(
        "timestamp",
        expireAfterSeconds=86400
    )

    # Logs expire after 30 days
    await db.logs.create_index(
        "timestamp",
        expireAfterSeconds=2592000
    )
