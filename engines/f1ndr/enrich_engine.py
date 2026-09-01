
from core.utils.logger import logger

class EnrichEngine:

    """
    Fourth pipeline step:
    - Adds metadata (tags, score, etc.)
    """

    def run(self, state):
        logger.info("[ENRICH] Enriching listings")

        enriched = []
        for item in state.deduped:
            item["score"] = self.compute_score(item)
            enriched.append(item)

        state.enriched = enriched
        return enriched

    def compute_score(self, item):
        score = 0
        if item["price"] > 0:
            score += 1
        if item["title"]:
            score += 1
        return score
