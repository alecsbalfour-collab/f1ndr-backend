class HTTPUtils:
    def build_headers(self, extra: dict = None) -> dict:
        base = {"User-Agent": "F1NDR/1.0"}
        if extra:
            base.update(extra)
        return base

    def build_params(self, params: dict) -> dict:
        return params or {}

http_utils = HTTPUtils()
