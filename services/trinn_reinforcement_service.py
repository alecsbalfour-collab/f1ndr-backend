class TrinnReinforcementService:
    def __init__(self):
        self.score = 0

    def apply_interaction(self, emotion_score):
        self.score += emotion_score // 10
        self.score = max(-500, min(500, self.score))

    def snapshot(self):
        return {"reinforcement_score": self.score}
