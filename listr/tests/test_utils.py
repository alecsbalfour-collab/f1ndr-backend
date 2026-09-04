from listr.utils.post_utils import apply_post_rules
from listr.utils.validate_utils import apply_validate_rules

def test_post_utils():
    out = apply_post_rules({"title": " Test "}, {"strip_whitespace": True})
    assert out["title"] == "Test"

def test_validate_utils():
    out = apply_validate_rules({"title": "A"}, {"check_price": True})
    assert out["valid"] is False
