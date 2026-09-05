# f1ndr-backend/unifiers/core/unifier_core.py
"""
Core unification logic.
"""

from unifiers.data.unifier_data import build_unified_listing
from unifiers.data.normalize_data import build_normalize_payload
from unifiers.data.transform_data import build_transform_payload


class UnifierCore:
    def __init__(self, state_repo, normalize_repo, transform_repo):
        self.state_repo = state_repo
        self.normalize_repo = normalize_repo
        self.transform_repo = transform_repo

    async def unify(self, raw: dict) -> dict:
        normalized = build_normalize_payload(raw)
        await self.normalize_repo.insert(normalized)

        transformed = build_transform_payload(normalized)
        await self.transform_repo.insert(transformed)

        unified = build_unified_listing(transformed)
        await self.state_repo.save_unified(unified)

        return unified
