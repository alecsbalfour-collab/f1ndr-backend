from module import f1ndr_backend

class SchedulerBootstrap:
    def __init__(self):
        self.scheduler = f1ndr_backend["scheduler"]["scheduler"]
        self.heartbeat = f1ndr_backend["scheduler"]["heartbeat"]
        self.watchdog = f1ndr_backend["scheduler"]["watchdog"]

    def start(self):
        self.scheduler.tick()
        self.heartbeat.beat()
        self.watchdog.check()

scheduler_bootstrap = SchedulerBootstrap()
