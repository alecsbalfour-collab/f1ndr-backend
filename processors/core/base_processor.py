class BaseProcessor:
    def __init__(self, base_config, logger, validator, exceptions, formatter):
        self.base_config = base_config
        self.logger = logger
        self.validator = validator
        self.exceptions = exceptions
        self.formatter = formatter

    def process(self, payload: dict) -> dict:
        if not self.base_config.defaults().get("enabled", True):
            self.logger.warning("Base processor disabled")
            return {"status": "disabled"}

        errors = self.validator.validate(payload)
        if errors:
            self.logger.error(f"Validation errors: {errors}")
            raise self.exceptions.ValidationException(str(errors))

        formatted = self.formatter.format_payload(payload)
        self.logger.info("Base processor completed")
        return {"status": "ok", "payload": formatted}
