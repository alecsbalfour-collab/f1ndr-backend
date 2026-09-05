from utils.exception_utils import ValidationException


def test_validation_exception():
    try:
        raise ValidationException("error")
    except ValidationException as e:
        assert str(e) == "error"
