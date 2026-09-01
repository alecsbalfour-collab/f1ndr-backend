from abc import ABC, abstractmethod

class ServiceInterface(ABC):
    """Base interface for all services."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute service logic."""
        pass
