# trinn/services/trinn_character_service.py

import json
import os


class TrinnCharacterService:
    def __init__(self, config_path="trinn/config/trinn_character.json"):
        self.config_path = config_path
        self.data = self._load()

    def _load(self):
        if not os.path.exists(self.config_path):
            return {
                "personality": {},
                "behavior": {},
                "appearance": {},
                "emotion_map": {},
                "animation": {}
            }

        with open(self.config_path, "r") as f:
            return json.load(f)

    def get_personality(self):
        return self.data.get("personality", {})

    def get_behavior(self):
        return self.data.get("behavior", {})

    def get_appearance(self):
        return self.data.get("appearance", {})

    def get_emotion_map(self):
        return self.data.get("emotion_map", {})

    def get_animation(self):
        return self.data.get("animation", {})
