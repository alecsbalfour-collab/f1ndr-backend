class PostUtils:
    def summarize(self, data: dict) -> dict:
        return {
            "title": data.get("title"),
            "preview": (data.get("body") or "")[:100],
        }

    def format_tags(self, tags) -> list:
        if not tags:
            return []
        return [t.lower().strip() for t in tags]


post_utils = PostUtils()
