
# f1ndr_backend/tests/ingestion/test_ingestion_replay.py
import sys
sys.path.append(".")
import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from f1ndr_backend.pipelines.ingestion_history import record_ingestion

TEST_DB = "f1ndr_test"
MONGO_URI = "mongodb://localhost:27017"  # or your test URI


@pytest.mark.asyncio
async def test_ingestion_replay_record():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[TEST_DB]

    await record_ingestion(db, source="test_source", count=5)

    doc = await db.ingestion_history.find_one({"source": "test_source"})
    assert doc is not None
    assert doc["count"] == 5
