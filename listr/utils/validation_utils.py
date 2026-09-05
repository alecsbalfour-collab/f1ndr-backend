class ValidationUtils:
    def is_empty(self, value) -> bool:
        return value is None or value == ""

    def missing_fields(self, data: dict, required: list) -> list:
        return [field for field in required if self.is_empty(data.get(field))]


validation_utils = ValidationUtils()
