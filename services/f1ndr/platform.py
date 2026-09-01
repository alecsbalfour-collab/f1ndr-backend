class PlatformsService:
    """
    Platform metadata, availability, and routing.
    """

    def get_supported(self):
        return ["kijiji", "facebook", "autotrader"]

    def validate(self, platforms):
        supported = self.get_supported()
        return [p for p in platforms if p in supported]
