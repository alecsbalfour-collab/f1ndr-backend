from .ingest_pipeline import ingestPipeline


def build_pipeline_module():
    ingest = ingestPipeline()
    return {
        "ingest": ingest,
    }


pipelines = build_pipeline_module()
