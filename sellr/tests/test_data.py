from sellr.data.listing_data import listing_rules
from sellr.data.update_data import update_rules
from sellr.data.remove_data import remove_rules

def test_listing_rules():
    assert listing_rules()["require_title"] is True

def test_update_rules():
    assert update_rules()["allow_partial_updates"] is True

def test_remove_rules():
    assert remove_rules()["mark_removed"] is True
