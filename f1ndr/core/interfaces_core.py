"""
Interfaces for f1ndr.
"""

class ScraperInterface:
    def fetch_for_query(self, query: str, filters: dict):
        raise NotImplementedError


class EngineInterface:
    def parse(self, raw: str):
        raise NotImplementedError


class ProcessorInterface:
    def extract_listings(self, dom):
        raise NotImplementedError


class UnifierInterface:
    def unify(self, listing: dict, source: str):
        raise NotImplementedError
