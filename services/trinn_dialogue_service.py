from config.trinn_personality_profiles import TRINN_PERSONALITY_PROFILES

class TrinnDialogueService:
    def __init__(self):
        self.personality = "default"

    def set_personality(self, profile):
        if profile in TRINN_PERSONALITY_PROFILES:
            self.personality = profile

    def get_personality(self):
        return self.personality

    def generate_response(self, user_message, state):
        profile = TRINN_PERSONALITY_PROFILES[self.personality]
        tone = profile["tone"]
        style = profile["style"]
        return f"[{tone} | {style} | state={state}] Trinn says: I heard you say: '{user_message}'."
