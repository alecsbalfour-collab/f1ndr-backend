# f1ndr-backend/trinn/core/controller_core.py
"""
TRINN controller layer.
"""

from trinn.core.service_core import TrinnService


class TrinnController:
    def __init__(self, service: TrinnService):
        self.service = service

    async def run_pipeline(self, payload: dict) -> dict:
        return await self.service.run_pipeline(payload)
