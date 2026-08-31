# trinn/services/trinn_dialogue_service.py

class TrinnDialogueService:
    def __init__(self):
        self.history = []

    def add_message(self, sender: str, text: str):
        self.history.append({"sender": sender, "text": text})
        if len(self.history) > 50:
            self.history.pop(0)

    def get_history(self):
        return self.history

    def last_user_message(self):
        for msg in reversed(self.history):
            if msg["sender"] == "user":
                return msg["text"]
        return None
