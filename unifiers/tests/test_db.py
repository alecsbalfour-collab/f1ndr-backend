# f1ndr-backend/unifiers/tests/test_db.py
import pytest
from unifiers.db.unifier_state import UnifierStateRepo


class FakeClient:
    def __init__(self):
        self.store = []

    def __getitem__(self, name):
        return self

    async def insert_one(self, doc):
        self.store.append(doc)

    def find(self, query):
        async def gen():
            for d in self.store:
                yield d
        return gen()


@pytest.mark.asyncio
async def test_unifier_state_repo():
    repo = UnifierStateRepo(FakeClient())
    await repo.save_unified({"id": 1})
    results = await repo.fetch_unified({})
    assert len(results) == 1
