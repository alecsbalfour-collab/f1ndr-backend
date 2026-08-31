# trinn/services/trinn_logging_service.py

import datetime

class TrinnLoggingService:
    def __init__(self):
        self.logs = []

    def log(self, message: str, level: str = "info"):
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "level": level,
            "message": message
        }
        self.logs.append(entry)
        if len(self.logs) > 200:
            self.logs.pop(0)
        return entry

    def get_logs(self, limit: int = 50):
        return self.logs[-limit:]
