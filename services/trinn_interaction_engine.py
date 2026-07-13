from services.trinn_controller import TrinnController
from services.trinn_memory_service import TrinnMemoryService
from services.trinn_dialogue_service import TrinnDialogueService
from services.trinn_emotion_service import TrinnEmotionService
from services.trinn_personality_engine import TrinnAdaptivePersonality
from services.trinn_reinforcement_service import TrinnReinforcementService

class TrinnInteractionEngine:
    def __init__(self):
        self.controller = TrinnController()
        self.memory = TrinnMemoryService()
        self.dialogue = TrinnDialogueService()
        self.emotion = TrinnEmotionService()
        self.personality_engine = TrinnAdaptivePersonality()
        self.reinforcement = TrinnReinforcementService()

    def analyze_tone(self, msg):
        msg = msg.lower()
        if any(w in msg for w in ["thanks", "love", "great", "awesome"]):
            return "positive"
        if any(w in msg for w in ["hate", "bad", "terrible", "stupid"]):
            return "negative"
        return "neutral"

    def handle_message(self, user_message):
        snapshot = self.controller.get_snapshot()
        state = snapshot["state"]

        tone = self.analyze_tone(user_message)
        self.emotion.apply_tone(tone)

        self.personality_engine.update(self.emotion.emotion, self.memory.snapshot())
        self.dialogue.set_personality(self.personality_engine.get_mode())

        response_text = self.dialogue.generate_response(user_message, state)

        self.memory.add_interaction(user_message, response_text, state)

        self.reinforcement.apply_interaction(self.emotion.score)

        contract = self.controller.get_contract(
            self.emotion.snapshot(),
            self.reinforcement.snapshot()
        )

        return {
            "state": state,
            "tone": tone,
            "emotion": self.emotion.snapshot(),
            "personality": self.dialogue.get_personality(),
            "response": response_text,
            "memory": self.memory.snapshot(),
            "reinforcement": self.reinforcement.snapshot(),
            "animation": self.controller.animation.snapshot(),
            "contract": contract
        }
