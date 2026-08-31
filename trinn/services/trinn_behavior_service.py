# trinn/services/trinn_behavior_service.py

from trinn.services.trinn_character_service import TrinnCharacterService


class TrinnBehaviorService:
    def __init__(self):
        self.character = TrinnCharacterService()

    def get_behavior(self):
        return self.character.get_behavior()

    def update_behavior(self, key: str, value):
        behavior = self.character.get_behavior()
        behavior[key] = value
        return behavior
