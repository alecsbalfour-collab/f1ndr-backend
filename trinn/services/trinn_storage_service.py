# trinn/services/trinn_storage_service.py

import json
import os


class TrinnStorageService:
    def __init__(self, base_path="trinn/data"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def save(self, filename: str, data: dict):
        path = os.path.join(self.base_path, filename)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return True

    def load(self, filename: str):
        path = os.path.join(self.base_path, filename)
        if not os.path.exists(path):
            return {}
        with open(path, "r") as f:
            return json.load(f)
