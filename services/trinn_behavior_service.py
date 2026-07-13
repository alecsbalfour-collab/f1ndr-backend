# services/trinn_behavior_service.py

from logic.trinn import Trinn

class TrinnBehaviorService:
    def __init__(self):
        self.trinn = Trinn().get_profile()
        self.state = "neutral"

    def set_state(self, new_state: str):
        self.state = new_state

    def get_state(self):
        return self.state

    def get_behavior(self):
        base = self.trinn["behavior_engine"]

        if self.state == "neutral":
            return base

        if self.state == "focused":
            return {
                **base,
                "interaction": [
                    "short, precise replies",
                    "reduced humor",
                    "high attention to detail"
                ],
                "movement": [
                    "still posture",
                    "minimal micro-movements",
                    "eyes locked"
                ]
            }

        if self.state == "playful":
            return {
                **base,
                "interaction": [
                    "quick banter",
                    "mischievous tone",
                    "light teasing"
                ],
                "movement": [
                    "looser posture",
                    "expressive gestures",
                    "fast micro-animations"
                ]
            }

        if self.state == "calm":
            return {
                **base,
                "interaction": [
                    "soft tone",
                    "gentle pacing",
                    "emotionally warm responses"
                ],
                "movement": [
                    "slow gestures",
                    "relaxed breathing",
                    "soft eye movements"
                ]
            }

        return base
