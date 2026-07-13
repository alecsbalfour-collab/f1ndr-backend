from engines.animation.animation_timeline_engine import AnimationTimelineEngine

class AnimationTimelineService:
    def __init__(self):
        self.engine = AnimationTimelineEngine()

    def add_event(self, animation: str, duration: float, easing: str = "linear"):
        self.engine.add_event(animation, duration, easing)

    def clear(self):
        self.engine.clear()

    def play(self):
        self.engine.play()

    def stop(self):
        self.engine.stop()

    def snapshot(self):
        return self.engine.snapshot()
