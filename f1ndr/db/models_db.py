class ListingModelDB:
    def __init__(self, data: dict):
        self.data = data

    def serialize(self) -> dict:
        return self.data


class SourceModelDB:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "url": self.url,
        }
