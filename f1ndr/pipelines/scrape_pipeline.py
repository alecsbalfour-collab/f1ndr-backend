class ScrapePipeline:
    def run(self, source: str, params: dict) -> dict:
        return {
            "source": source,
            "params": params,
            "status": "scrape_pipeline_executed",
        }

scrape_pipeline = ScrapePipeline()
