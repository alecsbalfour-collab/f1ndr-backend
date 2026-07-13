class AnimationTimelineEngine:
    def __init__(self):
        self.timeline = []
        self.current_frame = 0
        self.playing = False

    def add_event(self, animation: str, duration: float, easing: str = "linear"):
        self.timeline.append({
            "animation": animation,
            "duration": duration,
            "easing": easing
        })

    def clear(self):
        self.timeline = []
        self.current_frame = 0
        self.playing = False

    def play(self):
        self.playing = True
        self.current_frame = 0

    def stop(self):
        self.playing = False

    def snapshot(self):
        return {
            "playing": self.playing,
            "current_frame": self.current_frame,
            "timeline": self.timeline
        }
