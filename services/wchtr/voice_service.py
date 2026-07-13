from engines.wchtr.voice_engine import VoiceEngine

class VoiceService:
    def __init__(self):
        self.engine = VoiceEngine()

    def set_text(self, text: str):
        self.engine.set_text(text)

    def set_emotion(self, emotion: str):
        self.engine.set_emotion(emotion)

    def set_pace(self, pace: float):
        self.engine.set_pace(pace)

    def set_pitch(self, pitch: float):
        self.engine.set_pitch(pitch)

    def set_character(self, character: str):
        self.engine.set_character(character)

    def snapshot(self):
        return self.engine.snapshot()
