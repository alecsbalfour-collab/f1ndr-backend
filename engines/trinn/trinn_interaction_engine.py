# trinn/engines/trinn_interaction_engine.py

class TrinnInteractionEngine:
    def __init__(self):
        self.last_interaction = None

    def interact(self, interaction_type: str):
        self.last_interaction = interaction_type

    def snapshot(self):
        return {
            "last_interaction": self.last_interaction
        }
