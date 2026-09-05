class CoreInterface:
    def process(self, payload: dict) -> dict:
        raise NotImplementedError
