# db/utils/helpers_db.py

import uuid

def generate_db_id() -> str:
    """
    Generate a unique identifier for DB-layer operations.
    Mirrors helpers_utils.py and helpers_data.py.
    """
    return str(uuid.uuid4())


def to_upper_db(text: str) -> str:
    """
    Convert text to uppercase.
    Consistent with naming and behavior across layers.
    """
    return text.upper()
