from engines.f1ndr.core.f1ndr_controller import F1ndrController


class F1ndrRouter:
    def __init__(self):
        self.controller = F1ndrController()

    def handle(self, payload: dict):
        query = payload.get("query", "")
        return self.controller.search(query)
