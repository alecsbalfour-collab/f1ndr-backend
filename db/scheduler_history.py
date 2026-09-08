class SchedulerHistory:
    def __init__(self):
        self.logs = []

    def record_run(self, job_id, status, error=None):
        self.logs.append({"job_id": job_id, "status": status, "error": error})

scheduler_history = SchedulerHistory()
