class ValidateConfig:
    def rules(self) -> dict:
        return {
            "required_fields": ["title", "body"],
            "min_length": 5,
        }


validate_config = ValidateConfig()
