# trinn/engines/trinn_personality_engine.py

class TrinnPersonalityEngine:
    def __init__(self):
        self.personality = {
            "tone": "neutral",
            "style": "calm",
            "traits": []
        }

    def set_trait(self, trait: str):
        self.personality["traits"].append(trait)

    def set_tone(self, tone: str):
        self.personality["tone"] = tone

    def set_style(self, style: str):
        self.personality["style"] = style

    def snapshot(self):
        return {
            "personality": self.personality
        }
