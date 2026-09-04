from listr.utils.validation_utils import ValidationUtils
from utils.exceptions import ServiceError

validator = ValidationUtils()

def test_validate_required_success():
    item = {
        "id": "123",
        "title": "Test Title",
        "description": "Test Description"
    }
    assert validator.validate_required(item, ["id", "title", "description"]) is True

def test_validate_required_missing():
    item = {
        "id": "123",
        "title": "Test Title"
    }
    try:
        validator.validate_required(item, ["id", "title", "description"])
        assert False
    except ServiceError:
        assert True

def test_validate_length_success():
    item = {"description": "A" * 50}
    assert validator.validate_length(item, "description", min_len=1, max_len=100) is True

def test_validate_length_too_short():
    item = {"description": ""}
    try:
        validator.validate_length(item, "description", min_len=1)
        assert False
    except ServiceError:
        assert True

def test_validate_length_too_long():
    item = {"description": "A" * 600}
    try:
        validator.validate_length(item, "description", max_len=500)
        assert False
    except ServiceError:
        assert True
