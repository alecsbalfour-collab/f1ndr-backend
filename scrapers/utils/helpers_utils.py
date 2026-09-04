import uuid

def generate_scraper_id() -> str:
    return str(uuid.uuid4())

def to_upper_scraper(text: str) -> str:
    return text.upper()
