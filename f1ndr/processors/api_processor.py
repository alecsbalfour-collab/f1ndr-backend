class ApiProcessor:
    """
    Processor for API responses that are not JSON or HTML.
    Example: XML, custom text formats, or structured blobs.
    """

    def extract_listings(self, raw: str):
        listings = []

        # Very simple fallback: split lines
        for line in raw.splitlines():
            if ":" in line:
                title, value = line.split(":", 1)
                listings.append({
                    "title": title.strip(),
                    "price": "",
                    "url": "",
                    "platform": "api"
                })

        return listings
