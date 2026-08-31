from engines.f1ndr_engine import F1ndrEngine

class RendererService:
    def __init__(self):
        # Attach the main engine
        self.engine = F1ndrEngine()

    def render(self, payload):
        """
        Non-logic wrapper for rendering operations.
        - payload may include: { "query": <string>, "frame": <data>, ... }
        - No logic here. We simply pass the query to the engine.
        """
        query = payload.get("query", "")
        return self.engine.run({"query": query})
