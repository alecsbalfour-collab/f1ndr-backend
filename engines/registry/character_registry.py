class CharacterRegistryEngine:
    def __init__(self):
        self.state = {
            "characters": {},
            "log": []
        }

    def register_character(self, char_id: str, data: dict):
        self.state["characters"][char_id] = data
        self.state["log"].append(f"Registered character '{char_id}'")

    def update_character(self, char_id: str, data: dict):
        if char_id not in self.state["characters"]:
            self.state["log"].append(f"Attempted update on unknown character '{char_id}'")
            return

        self.state["characters"][char_id].update(data)
        self.state["log"].append(f"Updated character '{char_id}' with {data}")

    def remove_character(self, char_id: str):
        if char_id not in self.state["characters"]:
            self.state["log"].append(f"Attempted removal of unknown character '{char_id}'")
            return

        del self.state["characters"][char_id]
        self.state["log"].append(f"Removed character '{char_id}'")

    def get_character(self, char_id: str):
        return self.state["characters"].get(char_id, None)

    def snapshot(self):
        return self.state
