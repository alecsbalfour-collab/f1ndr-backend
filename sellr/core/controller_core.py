"""
sellr controller layer.
"""

from sellr.core.service_core import SellrService


class SellrController:
    def __init__(self):
        self.service = SellrService()

    def create_listing(self, payload: dict):
        return self.service.create_listing(payload)

    def update_listing(self, payload: dict):
        return self.service.update_listing(payload)

    def remove_listing(self, payload: dict):
        return self.service.remove_listing(payload)
