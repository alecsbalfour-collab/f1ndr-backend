def build_dialogue_contract(history):
    return {
        "count": len(history),
        "messages": history
    }
