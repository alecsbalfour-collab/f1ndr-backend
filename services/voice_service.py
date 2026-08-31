from engines.f1ndr_engine import F1ndrEngine

class VoiceService:
    def __init__(self):
        # Attach the main engine
        self.engine = F1ndrEngine()

    def process(self, payload):
        """
        Global voice wrapper.
        No logic here — simply forwards the query to F1ndrEngine.
        """
        query = payload.get("query", "")
        return self.engine.run({"query": query})
