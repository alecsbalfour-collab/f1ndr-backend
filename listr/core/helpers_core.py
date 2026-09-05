class CoreHelpers:
    def normalize(self, data: dict) -> dict:
        return {k: v for k, v in data.items() if v is not None}

    def safe_get(self, data: dict, key: str, default=None):
        return data.get(key, default)


core_helpers = CoreHelpers()
