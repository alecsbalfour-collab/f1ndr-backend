queue = []

def enqueue_job(job: dict):
    queue.append(job)

def dequeue_job():
    return queue.pop(0) if queue else None
