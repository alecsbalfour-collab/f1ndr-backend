# f1ndr-backend/unifiers/tests/test_core.py
import pytest
from unifiers.core.unifier_core import UnifierCore


class FakeRepo:
    def __init__(self):
        self.items = []

    async def insert(self, doc):
        self.items.append(doc)

    async def fetch(self, query):
        return self.items

    async def save_unified(self, doc):
        self.items.append(doc)


@pytest.mark.asyncio
async def test_unifier_core_unify():
    state = FakeRepo()
    norm = FakeRepo()
    trans = FakeRepo()
    core = UnifierCore(state_repo=state, normalize_repo=norm, transform_repo=trans)
    result = await core.unify({"id": 1, "title": "Test"})
    assert result.get("id") == 1
