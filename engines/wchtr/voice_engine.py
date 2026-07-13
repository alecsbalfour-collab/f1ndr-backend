class VoiceEngine:
    """
    Core engine for voice state management.
    This does NOT do TTS — it simply holds and updates the voice state.
    Your service layer or renderer layer can consume this snapshot.
    """

    def __init__(self):
        self.state = {
            "text": "",
            "emotion": "neutral",
            "pace": 1.0,
            "pitch": 1.0,
            "character": "default"
        }

    # -----------------------------
    # Setters
    # -----------------------------

    def set_text(self, text: str):
        self.state["text"] = text

    def set_emotion(self, emotion: str):
        self.state["emotion"] = emotion

    def set_pace(self, pace: float):
        self.state["pace"] = pace

    def set_pitch(self, pitch: float):
        self.state["pitch"] = pitch

    def set_character(self, character: str):
        self.state["character"] = character

    # -----------------------------
    # Snapshot
    # -----------------------------

    def snapshot(self):
        """
        Returns the current voice state.
        This is what your renderer or contract builder will consume.
        """
        return dict(self.state)
