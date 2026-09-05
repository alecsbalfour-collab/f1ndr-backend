from utils.formatter_utils import formatter_utils


def test_formatter_utils_trim():
    result = formatter_utils.format_payload({"field": " value "})
    assert result["field"] == "value"
