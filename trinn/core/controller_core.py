"""
Controller layer for trinn.
Routes incoming transformation/normalization/enrichment requests to the service layer.
"""

from typing import Dict, Any
from .service_core import TrinnService
from .helpers_core import normalize_key


class TrinnController:
    def __init__(self):
        self.service = TrinnService()

    def transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.service.transform(payload)

    def normalize(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.service.normalize(payload)

    def enrich(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.service.enrich(payload)
