# f1ndr_backend/pipelines/ingestion_history.py

import time
from motor.motor_asyncio import AsyncIOMotorDatabase

async def record_ingestion(db: AsyncIOMotorDatabase, source: str, count: int):
    """
    Records ingestion events for auditing, debugging, and analytics.
    """

    await db.ingestion_history.insert_one({
        "source": source,
        "count": count,
        "timestamp": time.time()
    })
