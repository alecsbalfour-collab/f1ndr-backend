class PlatformsEngine:
    DEFAULT_PLATFORMS = [
        "kijiji", "facebook", "autotrader", "craigslist",
        "usedca", "marketplace_ca", "ebay", "realtor",
        "rentfaster", "zillow"
    ]

    def run(self, requested_platforms):
        if not requested_platforms:
            return self.DEFAULT_PLATFORMS
        return [p for p in requested_platforms if p in self.DEFAULT_PLATFORMS]
