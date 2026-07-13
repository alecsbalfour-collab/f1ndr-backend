class TrinnMemoryService:
    def __init__(self):
        self.short_term = []
        self.long_term = []

    def add_interaction(self, user_message, trinn_response, state):
        entry = {
            "user_message": user_message,
            "trinn_response": trinn_response,
            "state": state,
        }
        self.short_term.append(entry)

        if len(self.short_term) > 20:
            self.long_term.append(self.short_term.pop(0))

    def snapshot(self):
        return {
            "short_term": self.short_term,
            "long_term": self.long_term,
        }
