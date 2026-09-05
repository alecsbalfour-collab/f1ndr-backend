class APIProcessor:
    def process(self, payload: dict) -> dict:
        return {
            "payload": payload,
            "status": "api_processor_executed",
        }

api_processor = APIProcessor()
