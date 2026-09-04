class RemoveRepo:
    def __init__(self, client):
        self.collection = client.removals

    def log(self, payload, output):
        entry = {
            "input": payload,
            "output": output,
            "status": "removed"
        }
        self.collection.insert_one(entry)
        return entry
