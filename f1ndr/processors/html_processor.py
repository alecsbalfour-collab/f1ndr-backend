class HTMLProcessor:
    def process(self, html: str) -> dict:
        return {
            "html": html,
            "status": "html_processor_executed",
        }

html_processor = HTMLProcessor()
