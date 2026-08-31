# trinn/services/trinn_voice_service.py

class TrinnVoiceService:
    def __init__(self):
        self.voice_profile = {
            "pitch": 1.0,
            "speed": 1.0,
            "tone": "neutral"
        }

    def get_voice(self):
        return self.voice_profile

    def update_voice(self, key: str, value):
        self.voice_profile[key] = value
        return self.voice_profile

    def apply_voice_to_text(self, text: str):
        tone = self.voice_profile.get("tone", "neutral")

        if tone == "calm":
            return text.replace("!", ".")
        if tone == "excited":
            return text + "!"
        if tone == "soft":
            return f"*{text}*"

        return text
