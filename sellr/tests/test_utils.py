from sellr.core.helpers_core import safe_get

def test_safe_get():
    assert safe_get({"a": 1}, "a") == 1
    assert safe_get({"a": 1}, "b", 5) == 5
