class TrinnAdaptivePersonality:
    def __init__(self):
        self.mode = "default"

    def update(self, emotion, memory_snapshot):
        short = memory_snapshot.get("short_term", [])

        if emotion == "happy" and len(short) > 5:
            self.mode = "playful"
        elif emotion == "upset":
            self.mode = "analyst"
        else:
            self.mode = "default"

    def get_mode(self):
        return self.mode
