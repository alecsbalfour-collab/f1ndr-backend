"""
lisTr controller layer.
"""

from listr.core.service_core import LisTrService


class LisTrController:
    def __init__(self):
        self.service = LisTrService()

    def post(self, payload: dict):
        return self.service.post(payload)

    def validate(self, payload: dict):
        return self.service.validate(payload)

    def delete(self, payload: dict):
        return self.service.delete(payload)

    def update(self, payload: dict):
        return self.service.update(payload)
