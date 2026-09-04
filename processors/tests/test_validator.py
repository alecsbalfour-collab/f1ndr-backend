import pytest
from processors.utils.validator_utils import ValidatorUtils


def test_ensure_text_valid():
    ValidatorUtils.ensure_text("valid text")


def test_ensure_text_invalid_type():
    with pytest.raises(TypeError):
        ValidatorUtils.ensure_text(123)


def test_ensure_text_empty():
    with pytest.raises(ValueError):
        ValidatorUtils.ensure_text("   ")
