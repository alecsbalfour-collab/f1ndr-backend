from engines.f1ndr_engine import F1ndrEngine

class WchtrVoiceService:
    def __init__(self):
        # Attach the main engine
        self.engine = F1ndrEngine()

    def process(self, payload):
        """
        Non-logic wrapper for WCHTR voice operations.
        - payload may include: { "query": <string>, "metadata": {...} }
        - No logic here. We simply pass the query to the engine.
        """
        query = payload.get("query", "")
        return self.engine.run({"query": query})
