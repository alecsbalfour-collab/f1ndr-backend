class PipelineConfig:
    def defaults(self) -> dict:
        return {
            "enabled": True,
            "max_batch": 100,
        }


pipeline_config = PipelineConfig()
