from scheduler.health import update_heartbeat

def run():
    update_heartbeat()
    print("Scheduler heartbeat: alive")
