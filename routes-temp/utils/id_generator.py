import uuid

def generate_id() -> str:
    """
    Generate a unique UUID string.
    """
    return str(uuid.uuid4())
