class F1ndrState:
    def __init__(self):
        self.last_query = None
        self.last_results = []

    def update(self, query, results):
        self.last_query = query
        self.last_results = results
