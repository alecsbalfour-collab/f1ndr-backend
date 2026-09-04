import uuid

def generate_id():
    """
    Generates a unique ID for internal API use.
    """
    return str(uuid.uuid4())
