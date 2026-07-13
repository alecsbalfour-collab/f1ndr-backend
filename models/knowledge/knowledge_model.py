def build_knowledge_contract(snapshot):
    return {
        "knowledge": {
            "facts": snapshot["facts"],
            "categories": snapshot["categories"]
        },
        "meta": {
            "engine": "KnowledgeEngine",
            "contract_type": "knowledge"
        }
    }
