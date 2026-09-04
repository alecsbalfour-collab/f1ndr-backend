from sellr.utils.listing_utils import apply_listing_rules
from sellr.utils.update_utils import apply_update_rules
from sellr.utils.remove_utils import apply_remove_rules

def test_listing_utils():
    out = apply_listing_rules({"title": " Test "}, {"strip_whitespace": True})
    assert out["title"] == "Test"

def test_update_utils():
    out = apply_update_rules({"title": " Test "}, {"strip_whitespace": True})
    assert out["title"] == "Test"

def test_remove_utils():
    out = apply_remove_rules({"id": "1"}, {"mark_removed": True})
    assert out["status"] == "removed"
