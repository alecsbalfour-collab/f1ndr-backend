class RegistryEngine:
    def __init__(self):
        self.state = {
            "items": {},
            "log": []
        }

    def register(self, key: str, value: dict):
        self.state["items"][key] = value
        self.state["log"].append(f"Registered '{key}'")

    def update(self, key: str, value: dict):
        if key not in self.state["items"]:
            self.state["log"].append(f"Attempted update on unknown key '{key}'")
            return

        self.state["items"][key].update(value)
        self.state["log"].append(f"Updated '{key}' with {value}")

    def remove(self, key: str):
        if key not in self.state["items"]:
            self.state["log"].append(f"Attempted removal of unknown key '{key}'")
            return

        del self.state["items"][key]
        self.state["log"].append(f"Removed '{key}'")

    def get(self, key: str):
        return self.state["items"].get(key, None)

    def snapshot(self):
        return self.state
