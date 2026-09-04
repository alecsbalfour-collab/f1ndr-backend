# tests/tests/test_tests.py

from tests.module import load_tests_system, run_tests_pipeline


def run_tests() -> str:
    """Minimal test suite for tests layer."""
    system = load_tests_system()

    assert "config" in system
    assert "environment" in system
    assert "connection" in system
    assert "utils" in system

    sample = {"x": 1}
    result = run_tests_pipeline(sample)

    assert result["tested"] is True

    return "All tests-layer tests passed."
