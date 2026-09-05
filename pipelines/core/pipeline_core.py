class PipelineCore:
    def __init__(self, config, data, state, logger):
        self.config = config
        self.data = data
        self.state = state
        self.logger = logger

    def process(self, payload: dict) -> dict:
        if not self.config.defaults().get("enabled", True):
            self.logger.warning("Pipeline disabled")
            return {"status": "disabled"}

        self.logger.info("Processing payload")
        self.state.increment_runs()

        return {
            "status": "ok",
            "payload": payload,
            "runs": self.state.runs,
        }
