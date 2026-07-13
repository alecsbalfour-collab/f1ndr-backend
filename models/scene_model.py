def build_scene_contract(context):
    return {
        "scene": {
            "location": context["location"],
            "time_of_day": context["time_of_day"],
            "weather": context["weather"],
            "characters": context["characters"],
            "objects": context["objects"],
            "mood": context["mood"]
        },
        "meta": {
            "engine": "SceneContextEngine",
            "contract_type": "scene_context"
        }
    }
