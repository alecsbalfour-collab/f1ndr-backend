class ServiceCore:
    def __init__(self, repo):
        self.repo = repo

    def create_post(self, data: dict) -> dict:
        return self.repo.create(data)

    def get_post(self, post_id: str) -> dict:
        return self.repo.get(post_id)
