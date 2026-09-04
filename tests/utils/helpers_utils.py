# tests/utils/helpers_utils.py

import uuid

def generate_tests_id() -> str:
    return str(uuid.uuid4())


def to_upper_tests(text: str) -> str:
    return text.upper()
