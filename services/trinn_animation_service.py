class TrinnAnimationService:
    def __init__(self):
        self.timeline = []
        self.current_animation = "idle"

    def set_animation(self, animation):
        self.current_animation = animation

    def add_timeline_event(self, animation, duration):
        self.timeline.append({
            "animation": animation,
            "duration": duration
        })

    def clear_timeline(self):
        self.timeline = []

    def snapshot(self):
        return {
            "current_animation": self.current_animation,
            "timeline": self.timeline
        }
