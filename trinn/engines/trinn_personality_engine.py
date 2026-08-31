# trinn/engines/trinn_personality_engine.py

class TrinnPersonalityEngine:
    def apply_personality(self, text, personality):
        style = personality.get("style", "neutral")

        if style == "calm":
            return text.replace("!", ".").strip()

        if style == "playful":
            return text + " 😏"

        return text
