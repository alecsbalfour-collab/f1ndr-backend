from services.trinn_animation_service import TrinnAnimationService

class TrinnAnimationEngine:
    def __init__(self):
        self.anim = TrinnAnimationService()

    def apply_state(self, state):
        if state == "focused":
            self.anim.set_animation("focus_idle")
        elif state == "relaxed":
            self.anim.set_animation("relaxed_breath")
        elif state == "playful":
            self.anim.set_animation("bounce")
        elif state == "calm":
            self.anim.set_animation("slow_idle")
        else:
            self.anim.set_animation("idle")

    def build_timeline(self, state):
        self.anim.clear_timeline()

        if state == "focused":
            self.anim.add_timeline_event("blink_fast", 1.2)
            self.anim.add_timeline_event("lean_forward", 2.0)

        elif state == "relaxed":
            self.anim.add_timeline_event("slow_blink", 2.5)
            self.anim.add_timeline_event("breath_cycle", 3.0)

        elif state == "playful":
            self.anim.add_timeline_event("head_tilt", 1.0)
            self.anim.add_timeline_event("bounce", 1.5)

        elif state == "calm":
            self.anim.add_timeline_event("soft_blink", 2.0)
            self.anim.add_timeline_event("micro_sway", 3.0)

        else:
            self.anim.add_timeline_event("idle", 2.0)

    def snapshot(self):
        return self.anim.snapshot()
