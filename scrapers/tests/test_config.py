# scrapers/tests/test_config.py

import pytest
from scrapers.core.data.environment_data import get_environment

def test_environment_returns_dict():
    env = get_environment()
    assert isinstance(env, dict)

def test_environment_has_required_keys():
    env = get_environment()
    assert "env" in env
    assert "debug" in env
    assert "version" in env
