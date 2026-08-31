# trinn/services/trinn_animation_service.py

from trinn.engines.trinn_animation_engine import TrinnAnimationEngine
from trinn.services.trinn_character_service import TrinnCharacterService


class TrinnAnimationService:
    def __init__(self):
        self.engine = TrinnAnimationEngine()
        self.character = TrinnCharacterService()

    def get_timeline(self, state: str):
        animation_config = self.character.get_animation()
        emotion_map = self.character.get_emotion_map()

        emotion_state = emotion_map.get("default", "neutral")

        return self.engine.generate_timeline(
            state,
            emotion_state,
            animation_config
        )
