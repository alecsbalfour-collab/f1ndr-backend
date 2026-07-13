def build_evolution_contract(snapshot):
    return {
        "evolution": {
            "traits": snapshot["traits"],
            "experience": snapshot["experience"],
            "level": snapshot["level"],
            "growth_log": snapshot["growth_log"]
        },
        "meta": {
            "engine": "EvolutionEngine",
            "contract_type": "evolution"
        }
    }
