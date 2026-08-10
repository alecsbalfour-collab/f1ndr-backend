class VoiceService:
    def generate(self, text: str):
        if not text:
            return {"error": "Missing text"}

        return {
            "engine": "global-voice",
            "input": text,
            "output": f"voice-output-for: {text}"
        }
