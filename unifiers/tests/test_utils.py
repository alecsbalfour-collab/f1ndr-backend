# f1ndr-backend/unifiers/tests/test_utils.py
from unifiers.utils.dict_utils import merge_dicts


def test_merge_dicts():
    base = {"a": 1}
    updates = {"b": 2}
    merged = merge_dicts(base, updates)
    assert merged["a"] == 1
    assert merged["b"] == 2
