# db/tests/test_db.py

from db.module import load_db_system, run_db_pipeline
from db.core.rules_db import is_valid_db_core_record
from db.Db.connection_db import ping_db_connection


def run_db_tests() -> str:
    """
    Minimal test suite for the DB layer.
    Mirrors the structure of core/tests/test_core.py and data/tests/test_data.py.
    """

    # Load DB system
    system = load_db_system()

    # Ensure subsystems exist
    assert "config" in system
    assert "environment" in system
    assert "connection" in system
    assert "utils" in system

    # Test DB pipeline rule normalization
    sample = {"key": "  TestKey  ", "value": "  TestValue  "}
    result = run_db_pipeline(sample)

    assert result["key"] == "TestKey"
    assert result["value"] == "TestValue"

    # Test DB record validation
    assert is_valid_db_core_record({"key": "Hello"})
    assert not is_valid_db_core_record({})

    # Test DB connection ping
    assert ping_db_connection(system["connection"]) is True

    return "All DB tests passed."
