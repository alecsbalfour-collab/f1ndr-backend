import json
from pathlib import Path

class Trinn:
    def __init__(self):
        base = Path(__file__).parent.parent
        json_path = base / "data" / "trinn_character.json"

        with open(json_path, "r") as f:
            self.data = json.load(f)

    def get_profile(self):
        return self.data

