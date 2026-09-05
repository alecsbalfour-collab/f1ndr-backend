class Watchdog:
    def __init__(self, logger, state, history):
        self.logger = logger
        self.state = state
        self.history = history

    def check(self):
        last_tick = self.state.last_tick
        last_heartbeat = self.state.last_heartbeat

        if last_tick is None or last_heartbeat is None:
            self.logger.warning("Watchdog: missing scheduler activity")
            return {"status": "warning"}

        self.logger.info("Watchdog check OK")
        return {"status": "ok"}
