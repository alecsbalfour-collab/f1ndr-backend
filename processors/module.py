from .normalize import NormalizeProcessor
from .categories import CategoriesProcessor


class ProcessorRegistry:
    def __init__(self):
        self._processors = {
            "normalize": NormalizeProcessor(),
            "categories": CategoriesProcessor(),
        }

    def get(self, name: str):
        if name not in self._processors:
            raise ValueError(f"Processor '{name}' not found.")
        return self._processors[name]

    def list(self):
        return list(self._processors.keys())


registry = ProcessorRegistry()
