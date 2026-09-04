from processors.interfaces.processor_interface import ProcessorInterface


class BaseProcessor(ProcessorInterface):
    """
    Enterprise-level base processor.
    Provides shared validation and naming behavior.
    """

    def __init__(self, config, core, db):
        self.config = config
        self.core = core
        self.db = db

    def validate(self, text: str):
        if not isinstance(text, str):
            raise TypeError("Processor input must be a string.")
        if not text.strip():
            raise ValueError("Processor input cannot be empty.")

    def name(self) -> str:
        return self.__class__.__name__
