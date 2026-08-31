# trinn/engines/trinn_behavior_engine.py

class TrinnBehaviorEngine:
    def apply_behavior(self, state: str, behavior_config: dict):
        if state in behavior_config:
            return {
                "action": behavior_config[state].get("action", "idle"),
                "speed": behavior_config[state].get("speed", 1.0)
            }
        return {"action": "idle", "speed": 1.0}
