class FormatterUtils:
    """
    Enterprise-level formatting utilities for processors.
    """

    @staticmethod
    def clean_whitespace(value: str) -> str:
        return " ".join(value.split())

    @staticmethod
    def trim(value: str) -> str:
        return value.strip()

    @staticmethod
    def normalize_case(value: str, lowercase: bool = True) -> str:
        return value.lower() if lowercase else value
