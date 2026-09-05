class DBUtils:
    def sanitize(self, document: dict) -> dict:
        return {k: v for k, v in document.items() if v is not None}

db_utils = DBUtils()
