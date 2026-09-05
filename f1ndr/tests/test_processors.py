def test_api_processor():
    from f1ndr.processors import api_processor
    result = api_processor.process({"key": "value"})
    assert result["status"] == "api_processor_executed"


def test_html_processor():
    from f1ndr.processors import html_processor
    result = html_processor.process("<html></html>")
    assert result["status"] == "html_processor_executed"
