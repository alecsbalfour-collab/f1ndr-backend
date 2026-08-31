# trinn/services/trinn_appearance_service.py

class TrinnAppearanceService:
    def __init__(self):
        self.appearance = {
            "theme": "default",
            "color": "blue",
            "style": "soft"
        }

    def set_theme(self, theme: str):
        self.appearance["theme"] = theme

    def snapshot(self):
        return {
            "appearance": self.appearance
        }
