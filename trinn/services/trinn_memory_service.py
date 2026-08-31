# trinn/services/trinn_memory_service.py

class TrinnMemoryService:
    def __init__(self):
        self.short_term = []
        self.long_term = []

    def remember(self, item: str):
        self.short_term.append(item)
        if len(self.short_term) > 10:
            self.long_term.append(self.short_term.pop(0))

    def get_recent(self):
        return self.short_term[-5:]

    def get_all(self):
        return {
            "short_term": self.short_term,
            "long_term": self.long_term
        }
