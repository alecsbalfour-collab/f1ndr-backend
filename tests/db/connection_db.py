# tests/Db/connection_db.py

def get_tests_connection() -> dict:
    """Mock DB connection for tests layer."""
    return {
        "connected": True,
        "driver": "mock-db",
    }


def ping_tests_connection(conn: dict) -> bool:
    return conn.get("connected", False)
