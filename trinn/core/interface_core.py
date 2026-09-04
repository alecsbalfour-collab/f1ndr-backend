"""
Interfaces for trinn core.
Defines abstract contracts for transformation pipelines.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class TransformInterface(ABC):
    @abstractmethod
    def transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass


class NormalizeInterface(ABC):
    @abstractmethod
    def normalize(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass


class EnrichInterface(ABC):
    @abstractmethod
    def enrich(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass
