from engines.voice.voice_engine import VoiceEngine

class VoiceService:
    def __init__(self):
        self.engine = VoiceEngine()

    def process(self, payload):
        return self.engine.run(payload)
