# f1ndr-backend/trinn/core/interface_core.py
"""
TRINN interface definitions.
"""

class RepoInterface:
    async def insert(self, doc: dict):
        raise NotImplementedError

    async def fetch(self, query: dict):
        raise NotImplementedError
