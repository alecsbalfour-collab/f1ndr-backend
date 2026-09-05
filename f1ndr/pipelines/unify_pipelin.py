class SearchPipeline:
    def run(self, query: dict) -> dict:
        return {
            "query": query,
            "status": "search_pipeline_executed",
        }

search_pipeline = SearchPipeline()
