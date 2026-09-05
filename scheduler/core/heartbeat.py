class Heartbeat:
    def __init__(self, logger, state, time_utils):
        self.logger = logger
        self.state = state
        self.time_utils = time_utils

    def beat(self):
        now = self.time_utils.now()
        self.state.update_last_heartbeat(now)
        self.logger.info(f"Heartbeat at {now}")
        return {"status": "ok", "timestamp": now}
