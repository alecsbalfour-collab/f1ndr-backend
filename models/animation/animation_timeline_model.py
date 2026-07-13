def build_animation_timeline_contract(snapshot):
    return {
        "animation_timeline": {
            "playing": snapshot["playing"],
            "current_frame": snapshot["current_frame"],
            "timeline": snapshot["timeline"]
        },
        "meta": {
            "engine": "AnimationTimelineEngine",
            "contract_type": "animation_timeline"
        }
    }
