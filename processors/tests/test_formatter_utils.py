from processors.utils.formatter_utils import FormatterUtils


def test_trim():
    assert FormatterUtils.trim("  hello  ") == "hello"


def test_clean_whitespace():
    assert FormatterUtils.clean_whitespace("hello   world") == "hello world"


def test_normalize_case():
    assert FormatterUtils.normalize_case("HELLO") == "hello"
