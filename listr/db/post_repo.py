class PostRepo:
    def __init__(self, client):
        self.collection = client.posts

    def log(self, payload, output):
        entry = {
            "input": payload,
            "output": output,
            "status": "posted"
        }
        self.collection.insert_one(entry)
        return entry
