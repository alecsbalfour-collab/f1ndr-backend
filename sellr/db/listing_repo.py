class ListingRepo:
    def __init__(self, client):
        self.collection = client.listings

    def log(self, payload, output):
        entry = {
            "input": payload,
            "output": output,
            "status": "created"
        }
        self.collection.insert_one(entry)
        return entry
