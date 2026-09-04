from processors.normalize import NormalizeProcessor


def test_normalize_basic():
    processor = NormalizeProcessor()
    result = processor.run("  Hello WORLD!!  ")
    assert result == "hello world"
