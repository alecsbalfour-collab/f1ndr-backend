from engines.dialogue.dialogue_engine import DialogueEngine

class DialogueService:
    def __init__(self):
        self.engine = DialogueEngine()

    def set_personality(self, personality: str):
        self.engine.set_personality(personality)

    def send_message(self, message: str):
        return self.engine.generate_reply(message)

    def history(self):
        return self.engine.snapshot()
