from engines.registry.character_registry import CharacterRegistry
from services.trinn_controller import TrinnController

class RegistryService:
    def __init__(self):
        self.registry = CharacterRegistry()

        # default characters
        self.registry.register("trinn", TrinnController())

    def add_character(self, name: str, controller):
        self.registry.register(name, controller)

    def remove_character(self, name: str):
        self.registry.unregister(name)

    def get_character(self, name: str):
        return self.registry.get(name)

    def list_characters(self):
        return self.registry.list()

    def snapshot(self):
        return self.registry.snapshot()
