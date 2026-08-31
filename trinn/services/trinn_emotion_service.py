# trinn/services/trinn_emotion_service.py

from trinn.services.trinn_character_service import TrinnCharacterService


class TrinnEmotionService:
    def __init__(self):
        self.character = TrinnCharacterService()
        self.current_emotion = "neutral"

    def get_emotion_map(self):
        return self.character.get_emotion_map()

    def set_emotion(self, emotion: str):
        self.current_emotion = emotion
        return self.current_emotion

    def get_emotion(self):
        return self.current_emotion
