class VoiceEngine:
    def __init__(self):
        self.voice_state = {
            "text": "",
            "emotion": "neutral",
            "pace": 1.0,
            "pitch": 1.0,
            "character": None
        }

    def set_text(self, text: str):
        self.voice_state["text"] = text

    def set_emotion(self, emotion: str):
        self.voice_state["emotion"] = emotion

    def set_pace(self, pace: float):
        self.voice_state["pace"] = pace

    def set_pitch(self, pitch: float):
        self.voice_state["pitch"] = pitch

    def set_character(self, character: str):
        self.voice_state["character"] = character

    def snapshot(self):
        return self.voice_state
