# trinn/engines/trinn_interaction_engine.py

class TrinnInteractionEngine:
    def evaluate_interaction(self, user_input, personality, behavior_map):
        text = user_input.lower()

        if any(x in text for x in ["help", "how", "what", "why"]):
            return "focused"

        if any(x in text for x in ["lol", "haha", "funny"]):
            return "playful"

        return personality.get("style", "neutral")
