from abc import ABC, abstractmethod

class EngineInterface(ABC):
    """Base interface for all engines."""

    @abstractmethod
    def run(self, *args, **kwargs):
        """Execute engine logic."""
        pass
