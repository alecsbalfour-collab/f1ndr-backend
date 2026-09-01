class NormalizeEngine:
    def run(self, listings):
        normalized = []

        for item in listings:
            normalized.append({
                "id": item.get("id"),
                "title": item.get("title", "").strip(),
                "price": float(item.get("price", 0)),
                "platform": item.get("platform"),
                "url": item.get("url"),
                "location": item.get("location", None)
            })

        return normalized
