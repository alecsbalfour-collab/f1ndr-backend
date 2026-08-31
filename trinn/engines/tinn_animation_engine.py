# trinn/engines/trinn_animation_engine.py

class TrinnAnimationEngine:
    def generate_timeline(self, behavior_state, emotion_state, animation_config):
        timelines = animation_config.get("timelines", {})
        default = animation_config.get("default_timeline", [])

        # Pick timeline by behavior first, fallback to default
        return timelines.get(behavior_state, default)
