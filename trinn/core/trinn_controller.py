# trinn/trinn_controller.py

from trinn.services.trinn_character_service import TrinnCharacterService
from trinn.engines.trinn_animation_engine import TrinnAnimationEngine
from trinn.engines.trinn_interaction_engine import TrinnInteractionEngine
from trinn.engines.trinn_personality_engine import TrinnPersonalityEngine


class TrinnController:
    def __init__(self):
        self.character = TrinnCharacterService()
        self.animation_engine = TrinnAnimationEngine()
        self.interaction_engine = TrinnInteractionEngine()
        self.personality_engine = TrinnPersonalityEngine()

        self.state = "neutral"

    def process_input(self, user_input: str):
        personality = self.character.get_personality()
        behavior = self.character.get_behavior()
        emotion = self.character.get_emotion_map()
        animation = self.character.get_animation()

        # Determine new state
        new_state = self.interaction_engine.evaluate_interaction(
            user_input,
            personality,
            behavior.get("states", {})
        )

        self.state = new_state

        # Generate animation timeline
        timeline = self.animation_engine.generate_timeline(
            new_state,
            emotion.get("default", "neutral"),
            animation
        )

        # Apply personality to text
        response = self.personality_engine.apply_personality(
            f"Trinn is now {new_state}.",
            personality
        )

        return {
            "state": new_state,
            "animation": timeline,
            "response": response
        }
