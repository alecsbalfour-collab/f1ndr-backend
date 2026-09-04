"""
sellr.module
Public entrypoint for the sellr selling engine.
"""

from sellr.core.controller_core import SellrController
from sellr.core.service_core import SellrService


class SellrModule:
    def __init__(self):
        self.controller = SellrController()
        self.service = SellrService()

    def create_listing(self, payload: dict):
        return self.controller.create_listing(payload)

    def update_listing(self, payload: dict):
        return self.controller.update_listing(payload)

    def remove_listing(self, payload: dict):
        return self.controller.remove_listing(payload)


sellr = SellrModule()
