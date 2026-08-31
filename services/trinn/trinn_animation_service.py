# trinn/services/trinn_animation_service.py

class TrinnAnimationService:
    def __init__(self):
        self.timeline = []
        self.current_state = "neutral"

    def apply_state(self, state: str):
        self.current_state = state

    def build_timeline(self, state: str):
        self.timeline = [f"animation_for_{state}"]

    def snapshot(self):
        return {
            "state": self.current_state,
            "timeline": self.timeline
        }
