import json
import os

class Trinn:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "..", "data", "trinn_character.json")

        with open(json_path, "r") as f:
            data = json.load(f)

        self.character = data.get("character", {})
        self.states = data.get("states", {})
        self.transitions = data.get("transitions", {})
        self.safety = data.get("safety", {})
        self.metadata = data.get("metadata", {})

        self.state = self.character.get("state", "idle")

    def get_profile(self):
        return {
            "name": self.character.get("name", "Unknown"),
            "state": self.state,
            "metadata": self.metadata
        }

    def _safety_check(self, text):
        max_len = self.safety.get("max_input_length", 500)
        blocked = self.safety.get("blocked_phrases", [])

        if len(text) > max_len:
            return False, "Input too long."

        lowered = text.lower()
        for phrase in blocked:
            if phrase in lowered:
                return False, self.safety.get("fallback_response", "I can't help with that.")

        return True, None

    def _resolve_transition(self, text):
        lowered = text.lower()

        for key, t in self.transitions.items():
            trigger = t.get("trigger")
            if trigger == "*" or trigger in lowered:
                if self.state in t.get("from", []):
                    return t

        return None

    def _apply_transition(self, transition):
        self.state = transition.get("to", self.state)
        return transition.get("response", "")

    def interact(self, text):
        safe, msg = self._safety_check(text)
        if not safe:
            return msg

        transition = self._resolve_transition(text)
        if not transition:
            return self.safety.get("fallback_response", "I’m not sure what you mean.")

        return self._apply_transition(transition)

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        if new_state in self.states:
            self.state = new_state

