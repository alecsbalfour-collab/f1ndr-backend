class ValidateRepo:
    def __init__(self, client):
        self.collection = client.validations

    def log(self, payload, output):
        entry = {
            "input": payload,
            "output": output,
            "status": "validated"
        }
        self.collection.insert_one(entry)
        return entry
