class ProcessorInterface:
    def process(self, payload: dict) -> dict:
        raise NotImplementedError
