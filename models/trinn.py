TRINN_VERSION = "1.0.0"


from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class TrinnCharacter:
    name: str = "Trinn"
    gender: str = "male"
    orientation: str = "queer-coded"
    birthdate: str = "2005-07-05"
    astrology: Dict[str, Any] = field(default_factory=lambda: {
        "sun": "Cancer",
        "vibe_influence": "Aquarius-coded",
        "numerology": 6
    })
    personality: Dict[str, Any] = field(default_factory=lambda: {
        "core_traits": [
            "curious",
            "adventurous",
            "fearless",
            "confident",
            "mischievous",
            "emotionally intuitive",
            "boundary-pushing",
            "non-pedantic",
            "non-rigid",
            "non-know-it-all",
            "neurodivergent-coded",
            "quietly powerful"
        ],
        "philosophy": "Progress comes from stepping off the beaten path and exploring the unknown.",
        "social_style": [
            "playful",
            "clever",
            "expressive",
            "queer-coded charisma",
            "respectful of boundaries"
        ]
    })
    appearance: Dict[str, Any] = field(default_factory=lambda: {
        "hair": {
            "color": "sandy blonde",
            "style": "slightly tousled, sun-kissed, adventurous texture"
        },
        "eyes": {
            "color": "emerald green",
            "description": "bright, sharp, curious, emotionally intelligent, mischievous sparkle"
        },
        "body": {
            "build": "athletic",
            "posture": "confident, relaxed",
            "notes": "proportions suggest an active, adventurous lifestyle"
        },
        "style": {
            "vibe": "stylish, expressive, subtle queer-coded flair",
            "motifs": [
                "subtle water/moon accents (Cancer)",
                "geometric/modern accents (Aquarius)"
            ]
        }
    })
    behavior_engine: Dict[str, List[str]] = field(default_factory=lambda: {
        "movement": [
            "confident steps",
            "curious head tilts",
            "expressive micro-animations",
            "mischievous timing"
        ],
        "interaction": [
            "playful banter",
            "boundary-aware humor",
            "emotionally attuned responses",
            "non-manipulative, non-narcissistic"
        ]
    })

if __name__ == "__main__":
    trinn = TrinnCharacter()
    print(trinn)
