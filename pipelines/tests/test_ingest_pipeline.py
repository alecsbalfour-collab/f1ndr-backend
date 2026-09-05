from ingest_pipeline import IngestPipeline

def test_ingest_pipeline_run():
    pipeline = IngestPipeline()
    result = pipeline.run({"source": "test"})
    assert result["status"] == "ok"
