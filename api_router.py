from error_handler import error_handler
from module import f1ndr_backend

class APIRouter:
    def __init__(self):
        self.backend = f1ndr_backend

    def route(self, path: str, payload: dict) -> dict:
        try:
            if path == "pipelines/ingest":
                return self.backend["pipelines"]["ingest"].run(payload)

            if path == "processors/base":
                return self.backend["processors"]["base"].process(payload)

            if path == "scheduler/tick":
                return self.backend["scheduler"]["scheduler"].tick()

            return {"status": "error", "message": "unknown route"}

        except Exception as e:
            return error_handler.handle(e)

api_router = APIRouter()
