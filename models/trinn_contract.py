TRINN_CONTRACT_VERSION = "4.0.0"

def build_trinn_contract(snapshot, memory, personality, emotion, reinforcement, animation):
    return {
        "version": TRINN_CONTRACT_VERSION,
        "state": snapshot["state"],
        "appearance": snapshot["appearance"],
        "behavior": snapshot["behavior"],
        "personality": personality,
        "emotion": emotion,
        "memory": memory,
        "reinforcement": reinforcement,
        "animation": animation,
        "render": {
            "face": snapshot["appearance"].get("face"),
            "eyes": snapshot["appearance"].get("eyes"),
            "hair": snapshot["appearance"].get("hair"),
            "outfit": snapshot["appearance"].get("outfit"),
            "animation": animation.get("current_animation"),
            "timeline": animation.get("timeline"),
            "interaction": snapshot["behavior"].get("interaction"),
        },
        "meta": {
            "engine": "Trinn",
            "contract_type": "character_intelligence",
            "supports": [
                "memory",
                "dialogue",
                "emotion",
                "adaptive_personality",
                "reinforcement",
                "animation_engine",
                "interaction_pipeline",
                "state_machine",
                "appearance_engine",
                "behavior_engine"
            ]
        }
    }
