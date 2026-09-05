class ValidationCore:
    def __init__(self, rules: dict):
        self.rules = rules

    def validate(self, data: dict) -> dict:
        missing = [
            field for field in self.rules.get("required_fields", [])
            if field not in data or not data[field]
        ]

        if missing:
            return {
                "status": "error",
                "missing_fields": missing,
            }

        return {"status": "ok"}
