from utils.validation_utils import validation_utils


def test_validator_empty_field():
    errors = validation_utils.validate({"field": ""})
    assert "field" in errors
