# f1ndr-backend/unifiers/core/service_core.py
"""
Unifiers service layer.
"""

from unifiers.core.unifier_core import UnifierCore


class UnifierService:
    def __init__(self, state_repo, normalize_repo, transform_repo):
        self.core = UnifierCore(
            state_repo=state_repo,
            normalize_repo=normalize_repo,
            transform_repo=transform_repo,
        )

    async def unify(self, raw: dict) -> dict:
        return await self.core.unify(raw)
