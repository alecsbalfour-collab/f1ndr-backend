class PipelineNormalize:
    def normalize(self, payload: dict) -> dict:
        return {
            k: (v.strip() if isinstance(v, str) else v)
            for k, v in payload.items()
        }
