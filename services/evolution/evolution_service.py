from engines.f1ndr_engine import F1ndrEngine

class EvolutionService:
    def __init__(self):
        # Attach the main engine
        self.engine = F1ndrEngine()

    def evolve(self, payload):
        """
        Non-logic wrapper for Evolution operations.
        - payload may include: { "query": <string>, "state": {...}, ... }
        - No logic here. We simply pass the query to the engine.
        """
        query = payload.get("query", "")
        return self.engine.run({"query": query})
