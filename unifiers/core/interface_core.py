# f1ndr-backend/unifiers/core/interface_core.py
"""
Unifiers interface definitions.
"""

class RepoInterface:
    async def insert(self, doc: dict):
        raise NotImplementedError

    async def fetch(self, query: dict):
        raise NotImplementedError
