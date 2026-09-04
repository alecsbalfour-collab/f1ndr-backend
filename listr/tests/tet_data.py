from listr.data.post_data import post_rules
from listr.data.validate_data import validate_rules

def test_post_rules():
    assert post_rules()["require_title"] is True

def test_validate_rules():
    assert validate_rules()["check_title"] is True
