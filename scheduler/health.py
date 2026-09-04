import time

last_heartbeat = 0

def update_heartbeat():
    global last_heartbeat
    last_heartbeat = time.time()

def get_heartbeat_age():
    return time.time() - last_heartbeat
