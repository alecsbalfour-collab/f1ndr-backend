class TrinnService:
    def process(self, text):
        if not text:
            return {"error": "Missing text"}

        return {
            "engine": "trinn",
            "input": text,
            "output": f"trinn-processed: {text}"
        }
