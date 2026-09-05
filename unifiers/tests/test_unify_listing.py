# f1ndr-backend/unifiers/tests/test_unify_listing.py
import pytest
from unifiers.unify_listing import unify_listing


@pytest.mark.asyncio
async def test_unify_listing_flow():
    result = await unify_listing("mongodb://localhost:27017", {"id": 1, "title": "Test"})
    assert result.get("id") == 1
    assert "title" in result
