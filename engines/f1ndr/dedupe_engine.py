class DedupeEngine:
    def dedupe(self, listings: list):
        seen = set()
        unique = []

        for item in listings:
            key = (
                item.get("title", "").lower(),
                item.get("price"),
                item.get("location", "").lower()
            )

            if key not in seen:
                seen.add(key)
                unique.append(item)

        return unique
