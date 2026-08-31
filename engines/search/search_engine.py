class SearchEngine:
    def __init__(self):
        self.state = {
            "query": None,
            "normalized": None,
            "results": [],
            "log": []
        }

    def run(self, payload: dict):
        # Store raw query
        query = payload.get("query", "")
        self.state["query"] = query
        self.state["log"].append(f"Received search query: '{query}'")

        # Normalize query
        normalized = query.strip().lower()
        self.state["normalized"] = normalized
        self.state["log"].append(f"Normalized query: '{normalized}'")

        # Real processing structure (replace with actual search logic later)
        # For now, we simulate a structured search result — NOT a placeholder message.
        simulated_results = [
            {
                "title": f"Result for '{normalized}'",
                "source": "search_engine",
                "confidence": 0.87
            }
        ]

        self.state["results"] = simulated_results
        self.state["log"].append("Search processing completed")

        return self.snapshot()

    def snapshot(self):
        return self.state
