class F1ndrEvents:
    def on_search_started(self, query):
        print(f"[f1ndr] Search started: {query}")

    def on_search_finished(self, query, count):
        print(f"[f1ndr] Search finished: {query} ({count} results)")
