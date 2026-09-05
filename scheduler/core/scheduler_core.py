class SchedulerCore:
    def __init__(self, config, intervals, state, history, logger, time_utils):
        self.config = config
        self.intervals = intervals
        self.state = state
        self.history = history
        self.logger = logger
        self.time_utils = time_utils

    def tick(self):
        if not self.config.defaults().get("enabled", True):
            self.logger.warning("Scheduler disabled")
            return {"status": "disabled"}

        now = self.time_utils.now()
        self.state.update_last_tick(now)
        self.logger.info(f"Scheduler tick at {now}")

        return {"status": "ok", "timestamp": now}
