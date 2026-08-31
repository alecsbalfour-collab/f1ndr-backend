# trinn/services/trinn_appearance_service.py

from trinn.services.trinn_character_service import TrinnCharacterService


class TrinnAppearanceService:
    def __init__(self):
        self.character = TrinnCharacterService()

    def get_appearance(self):
        return self.character.get_appearance()

    def update_appearance(self, key: str, value):
        appearance = self.character.get_appearance()
        appearance[key] = value
        return appearance
