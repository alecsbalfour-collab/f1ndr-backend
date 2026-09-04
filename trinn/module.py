"""
trinn.module
Module entrypoint for the Trinn system.

Trinn handles transformation, normalization, and enrichment pipelines.
This module exposes the TrinnController and TrinnService so other modules
(f1ndr, lisTr, sellr, watchr) can use Trinn without internal imports.

Dict‑based architecture. No engines. No processors. No scrapers.
"""

from trinn.core.controller_core import TrinnController
from trinn.core.service_core import TrinnService


class TrinnModule:
    """
    Public-facing module wrapper.
    Other modules import this class to interact with Trinn.
    """

    def __init__(self):
        self.controller = TrinnController()
        self.service = TrinnService()

    # Convenience passthroughs
    def transform(self, payload: dict):
        return self.controller.transform(payload)

    def normalize(self, payload: dict):
        return self.controller.normalize(payload)

    def enrich(self, payload: dict):
        return self.controller.enrich(payload)


# Singleton-style instance for global access
trinn = TrinnModule()
