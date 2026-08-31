# trinn/services/trinn_dialogue_service.py

class TrinnDialogueService:
    def __init__(self):
        self.personality = {
            "tone": "neutral",
            "style": "calm",
            "traits": []
        }

    def get_personality(self):
        return self.personality

    def snapshot(self):
        return {
            "personality": self.personality
        }
