class SchedulerHistory:
    def __init__(self):
        self.entries = []

    def record(self, entry: dict):
        self.entries.append(entry)
        return entry


scheduler_history = SchedulerHistory()
