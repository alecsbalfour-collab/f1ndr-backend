class SearchEngine:
    def run(self, query: str):
        return {
            "query": query.strip(),
            "filters": {},
            "platforms": None
        }
