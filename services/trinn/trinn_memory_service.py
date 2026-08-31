# trinn/services/trinn_memory_service.py

class TrinnMemoryService:
    def __init__(self):
        self.memory = {}

    def remember(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key)

    def snapshot(self):
        return {
            "memory": self.memory
        }
