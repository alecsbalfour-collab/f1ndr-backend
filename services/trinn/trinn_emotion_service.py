# trinn/services/trinn_emotion_service.py

class TrinnEmotionService:
    def __init__(self):
        self.emotion = "neutral"

    def set_emotion(self, emotion: str):
        self.emotion = emotion

    def snapshot(self):
        return {
            "emotion": self.emotion
        }
