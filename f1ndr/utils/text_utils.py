class TextUtils:
    def clean(self, text: str) -> str:
        return text.strip() if isinstance(text, str) else text

    def lower(self, text: str) -> str:
        return text.lower() if isinstance(text, str) else text

text_utils = TextUtils()
