class DedupeEngine:
    def run(self, listings):
        seen = set()
        deduped = []

        for item in listings:
            key = (item["title"].lower(), item["price"])
            if key not in seen:
                seen.add(key)
                deduped.append(item)

        return deduped
