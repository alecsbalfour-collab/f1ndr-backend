import json
import os

class Trinn:
    def __init__(self):
        # Correct path — works locally AND on Render
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "..", "data", "trinn_character.json")

        # Normalize path for Render
        json_path = os.path.normpath(json_path)

        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Missing JSON file: {json_path}")

        with open(json_path, "r") as f:
            self.character_data = json.load(f)

        # Basic state
        self.state = self.character_data.get("state", "idle")
        self.character = self.character_data.get("character", "default")

    def get_state(self):
        return {
            "character": self.character,
            "state": self.state
        }

    def set_state(self, new_state):
        self.state = new_state
        return {
            "character": self.character,
            "state": self.state
        }

    def interact(self, input_text):
        # Placeholder logic — replace with your real engine rules
        if "hello" in input_text.lower():
            self.state = "greeting"
            return {
                "response": "Hello! How can I help?",
                "state": self.state
            }

        if "bye" in input_text.lower():
            self.state = "idle"
            return {
                "response": "Goodbye!",
                "state": self.state
            }

        # Default fallback
        return {
            "response": "I’m not sure what you mean.",
            "state": self.state
        }
