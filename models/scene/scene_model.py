def build_scene_contract(data):
    return {
        "scene_id": data.get("scene_id", "unknown"),
        "characters": data.get("characters", []),
        "dialogue": data.get("dialogue", []),
        "metadata": data.get("metadata", {})
    }
