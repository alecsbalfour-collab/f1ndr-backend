"""
Interfaces for watchr core.
Defines abstract contracts for watcher and trigger components.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class WatchInterface(ABC):
    @abstractmethod
    def handle_watch_event(self, key: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass


class TriggerInterface(ABC):
    @abstractmethod
    def trigger_event(self, event: str, data: Dict[str, Any]) -> Dict[str, Any]:
        pass
