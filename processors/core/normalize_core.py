import re


class NormalizeCore:
    """
    Core normalization logic.
    Applies whitespace, casing, and character rules.
    """

    def __init__(self, config):
        self.config = config

    def process(self, text: str) -> str:
        if self.config.strip_whitespace:
            text = text.strip()

        if self.config.lowercase:
            text = text.lower()

        if self.config.remove_special_chars:
            text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

        if self.config.collapse_spaces:
            text = re.sub(r"\s+", " ", text)

        return text
