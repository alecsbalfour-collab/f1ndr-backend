class ServiceInterface:
    def create_post(self, data: dict) -> dict:
        raise NotImplementedError

    def get_post(self, post_id: str) -> dict:
        raise NotImplementedError


class ValidatorInterface:
    def validate(self, data: dict) -> dict:
        raise NotImplementedError
