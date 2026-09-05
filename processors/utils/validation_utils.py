class ValidationUtils:
    def validate(self, payload: dict) -> dict:
        errors = {}
        for key, value in payload.items():
            if value is None or value == "":
                errors[key] = "empty"
        return errors


validation_utils = ValidationUtils()
