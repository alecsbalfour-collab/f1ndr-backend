# f1ndr-backend/unifiers/core/controller_core.py
"""
Unifiers controller layer.
"""

from unifiers.core.service_core import UnifierService


class UnifierController:
    def __init__(self, service: UnifierService):
        self.service = service

    async def unify(self, payload: dict) -> dict:
        return await self.service.unify(payload)
