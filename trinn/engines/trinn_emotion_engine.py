# trinn/engines/trinn_emotion_engine.py

class TrinnEmotionEngine:
    def detect_emotion(self, text: str):
        text = text.lower()

        if any(x in text for x in ["happy", "great", "awesome"]):
            return "happy"
        if any(x in text for x in ["sad", "upset", "bad"]):
            return "sad"
        if any(x in text for x in ["angry", "mad", "frustrated"]):
            return "angry"

        return "neutral"

    def map_emotion(self, emotion: str, emotion_map: dict):
        return emotion_map.get(emotion, {"intensity": 0.5})
