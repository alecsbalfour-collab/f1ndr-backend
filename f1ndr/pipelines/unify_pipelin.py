"""
Unify Pipeline
Takes raw listings and unifies them without scraping.
Useful for testing unifier + trinn.
"""

from trinn.module import trinn


class UnifyPipeline:
    def __init__(self, unifier):
        self.unifier = unifier

    def run(self, raw_listings: list, source: str):
        unified = [self.unifier.unify(item, source) for item in raw_listings]
        transformed = [trinn.transform(item) for item in unified]
        return transformed
