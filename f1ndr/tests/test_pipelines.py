def test_scrape_pipeline():
    from f1ndr.pipelines import scrape_pipeline
    result = scrape_pipeline.run("autotrader", {"q": "cars"})
    assert result["status"] == "scrape_pipeline_executed"


def test_search_pipeline():
    from f1ndr.pipelines import search_pipeline
    result = search_pipeline.run({"q": "rentals"})
    assert result["status"] == "search_pipeline_executed"


def test_unify_pipeline():
    from f1ndr.pipelines import unify_pipeline
    result = unify_pipeline.run({"id": 1})
    assert result["status"] == "unify_pipeline_executed"
