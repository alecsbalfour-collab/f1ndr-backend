"""
f1ndr controller layer.
Coordinates search, scraping, and unification.
"""

from f1ndr.core.service_core import F1ndrService


class F1ndrController:
    def __init__(self):
        self.service = F1ndrService()

    def search(self, payload: dict):
        """
        Entrypoint for search requests.
        payload: {
            "query": "...",
            "sources": ["kijiji", "facebook", ...],
            "filters": {...}
        }
        """
        return self.service.search(payload)
