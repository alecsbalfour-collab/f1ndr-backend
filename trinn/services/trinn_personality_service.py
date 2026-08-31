# trinn/services/trinn_personality_service.py

from trinn.services.trinn_character_service import TrinnCharacterService


class TrinnPersonalityService:
    def __init__(self):
        self.character = TrinnCharacterService()

    def get_personality(self):
        return self.character.get_personality()

    def update_personality(self, key: str, value):
        personality = self.character.get_personality()
        personality[key] = value
        return personality

    def apply_to_text(self, text: str):
        personality = self.character.get_personality()
        style = personality.get("style", "neutral")

        if style == "calm":
            return text.replace("!", ".")
        if style == "playful":
            return text + " 😏"
        if style == "soft":
            return f"*{text}*"

        return text
