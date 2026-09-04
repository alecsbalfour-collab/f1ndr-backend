class UpdateRepo:
    def __init__(self, client):
        self.collection = client.updates

    def log(self, payload, output):
        entry = {
            "input": payload,
            "output": output,
            "status": "updated"
        }
        self.collection.insert_one(entry)
        return entry
