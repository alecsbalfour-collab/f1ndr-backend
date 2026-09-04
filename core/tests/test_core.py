# core/tests/test_core.py

from core.module import load_core_system, run_core_pipeline
from core.core.rules_core import is_valid_title

def run_tests() -> str:
    """Minimal test suite."""
    system = load_core_system()
    assert "config" in system
    assert "data" in system
    assert "db" in system

    sample = {"title": "  Test  "}
    result = run_core_pipeline(sample)
    assert result["title"] == "Test"

    assert is_valid_title("Hello")
    assert not is_valid_title("   ")

    return "All core tests passed."
