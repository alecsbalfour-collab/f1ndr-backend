from .base_config import BaseConfig


class CategoriesConfig(BaseConfig):
    """
    Configuration for CategoriesProcessor.
    """

    enable_keyword_matching: bool = True
    enable_rule_engine: bool = True
    min_length_for_long_text: int = 100

    def __init__(self, **overrides):
        super().__init__(**overrides)
