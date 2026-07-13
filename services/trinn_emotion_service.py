class TrinnEmotionService:
    def __init__(self):
        self.emotion = "neutral"

    def get_emotion(self):
        return self.emotion

    def set_emotion(self, new_emotion):
        self.emotion = new_emotion
        return self.emotion
