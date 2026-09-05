class ControllerCore:
    def __init__(self, service, validator):
        self.service = service
        self.validator = validator

    def create_post(self, data: dict) -> dict:
        validation = self.validator.validate(data)
        if validation.get("status") != "ok":
            return validation

        return self.service.create_post(data)

    def get_post(self, post_id: str) -> dict:
        return self.service.get_post(post_id)
