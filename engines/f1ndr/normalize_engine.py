class NormalizeEngine:
    def normalize(self, raw: dict):
        return {
            "id": raw.get("id"),
            "title": raw.get("title", "").strip(),
            "price": raw.get("price"),
            "location": raw.get("location", ""),
            "description": raw.get("description", ""),
            "images": raw.get("images", []),
            "platform": raw.get("platform", "unknown"),
            "url": raw.get("url"),
            "posted": raw.get("posted"),
            "raw": raw
        }
