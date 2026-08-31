# trinn/trinn_brain.py

from trinn.engines.trinn_interaction_engine import TrinnInteractionEngine
from trinn.engines.trinn_personality_engine import TrinnPersonalityEngine
from trinn.engines.trinn_behavior_engine import TrinnBehaviorEngine
from trinn.engines.trinn_emotion_engine import TrinnEmotionEngine
from trinn.engines.trinn_voice_engine import TrinnVoiceEngine
from trinn.engines.trinn_animation_engine import TrinnAnimationEngine

from trinn.services.trinn_character_service import TrinnCharacterService
from trinn.trinn_state_machine import TrinnStateMachine
from trinn.trinn_events import TrinnEvent


class TrinnBrain:
    def __init__(self):
        self.interaction = TrinnInteractionEngine()
        self.personality = TrinnPersonalityEngine()
        self.behavior = TrinnBehaviorEngine()
        self.emotion = TrinnEmotionEngine()
        self.voice = TrinnVoiceEngine()
        self.animation = TrinnAnimationEngine()

        self.character = TrinnCharacterService()
        self.state_machine = TrinnStateMachine()

    def think(self, text: str):
        # Detect intent
        intent = self.interaction.process_input(text)["intent"]
        event = getattr(TrinnEvent, intent.upper(), TrinnEvent.UNKNOWN)

        # State transition
        state = self.state_machine.transition(event)

        # Emotion detection + mapping
        emotion = self.emotion.detect_emotion(text)
        emotion_profile = self.emotion.map_emotion(
            emotion,
            self.character.get_emotion_map()
        )

        # Behavior
        behavior = self.behavior.apply_behavior(
            state,
            self.character.get_behavior()
        )

        # Personality style
        personality_output = self.personality.apply(
            text,
            self.character.get_personality()
        )

        # Voice output
        voice_output = self.voice.synthesize(
            personality_output,
            self.character.get_personality()
        )

        # Animation timeline
        animation = self.animation.generate_timeline(
            state=state,
            emotion=emotion,
            animation_config=self.character.get_animation()
        )

        return {
            "state": state,
            "emotion": emotion_profile,
            "behavior": behavior,
            "output": personality_output,
            "voice": voice_output,
            "animation": animation
        }
