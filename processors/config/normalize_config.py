from .base_config import BaseConfig


class NormalizeConfig(BaseConfig):
    """
    Configuration for NormalizeProcessor.
    """

    strip_whitespace: bool = True
    lowercase: bool = True
    remove_special_chars: bool = True
    collapse_spaces: bool = True

    def __init__(self, **overrides):
        super().__init__(**overrides)
