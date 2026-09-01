from abc import ABC, abstractmethod

class ModelInterface(ABC):
    """Base interface for data models."""

    @abstractmethod
    def to_dict(self):
        """Convert model to dictionary."""
        pass
