class RendererService:
    def render(self, frame):
        if not frame:
            return {"error": "Missing frame"}

        return {
            "engine": "global-renderer",
            "input": frame,
            "output": "rendered-global-frame"
        }
