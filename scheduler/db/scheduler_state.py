class SchedulerState:
    def __init__(self):
        self.last_tick = None
        self.last_heartbeat = None

    def update_last_tick(self, ts):
        self.last_tick = ts

    def update_last_heartbeat(self, ts):
        self.last_heartbeat = ts


scheduler_state = SchedulerState()
