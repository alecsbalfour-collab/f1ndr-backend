import random

class DialogueEngine:
    def __init__(self):
        self.history = []
        self.personality = "default"

    def set_personality(self, personality: str):
        self.personality = personality

    def add_message(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def generate_reply(self, user_message: str):
        self.add_message("user", user_message)

        # Placeholder LLM logic — replace with real model later
        reply = f"[{self.personality}] Response to: {user_message}"

        self.add_message("assistant", reply)
        return reply

    def snapshot(self):
        return {
            "personality": self.personality,
            "history": self.history
        }
