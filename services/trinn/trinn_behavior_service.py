# trinn/services/trinn_behavior_service.py

class TrinnBehaviorService:
    def __init__(self):
        self.behavior = "neutral"

    def set_behavior(self, behavior: str):
        self.behavior = behavior

    def snapshot(self):
        return {
            "behavior": self.behavior
        }
