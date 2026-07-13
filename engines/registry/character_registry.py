class CharacterRegistry:
    def __init__(self):
        self.characters = {}

    def register(self, name: str, controller):
        self.characters[name] = controller

    def unregister(self, name: str):
        if name in self.characters:
            del self.characters[name]

    def get(self, name: str):
        return self.characters.get(name)

    def list(self):
        return list(self.characters.keys())

    def snapshot(self):
        return {
            "characters": self.list()
        }
