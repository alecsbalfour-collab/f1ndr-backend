from datetime import datetime

class TimeUtils:
    def now(self):
        return datetime.utcnow().isoformat()


time_utils = TimeUtils()
