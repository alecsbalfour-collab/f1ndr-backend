"""
Service layer for trinn.
Handles transformation, normalization, and enrichment pipelines.
Pure dict‑based processing. No engines. No ORM. No Pydantic.
"""

from typing import Dict, Any
from .helpers_core import safe_get, normalize_key
from .exceptions_core import TrinnError


class TrinnService:
    def transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generic transformation pipeline.
        """
        return {
            "input": payload,
            "output": payload,  # placeholder for actual transform logic
            "status": "transformed"
        }

    def normalize(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize fields, casing, structure.
        """
        normalized = {normalize_key(k): v for k, v in payload.items()}
        return {
            "input": payload,
            "output": normalized,
            "status": "normalized"
        }

    def enrich(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add missing fields, computed values, metadata.
        """
        enriched = payload.copy()
        enriched["_enriched"] = True

        return {
            "input": payload,
            "output": enriched,
            "status": "enriched"
        }
