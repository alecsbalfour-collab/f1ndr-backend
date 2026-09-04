class ValidatorUtils:
    """
    Enterprise-level validation utilities for processors.
    """

    @staticmethod
    def ensure_text(value):
        if not isinstance(value, str):
            raise TypeError("Processor input must be a string.")
        if not value.strip():
            raise ValueError("Processor input cannot be empty.")
