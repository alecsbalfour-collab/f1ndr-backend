# f1ndr_backend/scheduler/cleanup_jobs.py

import time
from motor.motor_asyncio import AsyncIOMotorDatabase

CLEANUP_THRESHOLD_SECONDS = 7 * 24 * 3600  # 7 days


async def cleanup_ingestion_temp(db: AsyncIOMotorDatabase):
    """
    Removes temporary ingestion artifacts older than 7 days.
    """
    cutoff = time.time() - CLEANUP_THRESHOLD_SECONDS

    await db.ingestion_temp.delete_many({
        "timestamp": {"$lt": cutoff}
    })


async def cleanup_old_logs(db: AsyncIOMotorDatabase):
    """
    Removes old logs older than 30 days.
    """
    cutoff = time.time() - (30 * 24 * 3600)

    await db.logs.delete_many({
        "timestamp": {"$lt": cutoff}
    })
