def build_dialogue_contract(snapshot):
    return {
        "dialogue": {
            "personality": snapshot["personality"],
            "history": snapshot["history"]
        },
        "meta": {
            "engine": "DialogueEngine",
            "contract_type": "dialogue"
        }
    }
