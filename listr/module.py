"""
lisTr.module
Public entrypoint for the lisTr posting engine.

Exposes LisTrController and LisTrService for external modules
(f1ndr, trinn, sellr, watchr) to use without internal imports.
"""

from listr.core.controller_core import LisTrController
from listr.core.service_core import LisTrService


class LisTrModule:
    def __init__(self):
        self.controller = LisTrController()
        self.service = LisTrService()

    # Convenience passthroughs
    def post(self, payload: dict):
        return self.controller.post(payload)

    def validate(self, payload: dict):
        return self.controller.validate(payload)

    def delete(self, payload: dict):
        return self.controller.delete(payload)

    def update(self, payload: dict):
        return self.controller.update(payload)


# Singleton instance
listr = LisTrModule()
