class NormalizeCore:
    def __init__(self, config, db, logger):
        self.config = config
        self.db = db
        self.logger = logger

    def normalize(self, payload: dict) -> dict:
        self.logger.info("Normalizing payload")
        normalized = {
            k: (v.strip() if isinstance(v, str) else v)
            for k, v in payload.items()
        }
        self.db.store(normalized)
        return normalized
