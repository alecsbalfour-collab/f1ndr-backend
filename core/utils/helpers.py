def safe_get(data: dict, key: str, default=None):
    """Safely get a key from a dict."""
    return data.get(key, default)

def chunk_list(items: list, size: int):
    """Split list into chunks."""
    for i in range(0, len(items), size):
        yield items[i:i + size]

def flatten(list_of_lists):
    """Flatten nested lists."""
    return [item for sub in list_of_lists for item in sub]
