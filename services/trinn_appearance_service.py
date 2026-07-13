# services/trinn_appearance_service.py

from logic.trinn import Trinn

class TrinnAppearanceService:
    def __init__(self):
        self.trinn = Trinn().get_profile()
        self.state = "default"

    def get_appearance(self):
        return self.trinn["appearance"]

    def set_state(self, new_state: str):
        self.state = new_state

    def get_stateful_appearance(self):
        base = self.trinn["appearance"]

        if self.state == "default":
            return base

        if self.state == "focused":
            return {
                **base,
                "eyes": {
                    **base["eyes"],
                    "description": "emerald green, sharp, locked-in focus"
                }
            }

        if self.state == "relaxed":
            return {
                **base,
                "hair": {
                    **base["hair"],
                    "style": "looser, softer, relaxed texture"
                }
            }

        return base
