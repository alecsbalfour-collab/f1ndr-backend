class SchedulerState:
    def __init__(self):
        self.active_jobs = {}
        self.last_heartbeat = None

    def get_state(self):
        return {"status": "operational", "jobs_count": len(self.active_jobs)}

scheduler_state = SchedulerState()
