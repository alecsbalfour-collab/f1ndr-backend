from scrapers import (
    kijiji,
    autotrader,
    rentfaster,
    used_ca,
    realtor,
    zillow,
    ebay,
)
from db.mongo import get_listings_collection
from db.platforms import mark_success, mark_failure

from processors.normalize import normalize_listing
from processors.categorize import categorize_listing
from processors.score import score_listing
from processors.detect_spam import is_spam
from processors.demographics import infer_demographics


def run_all():
    col = get_listings_collection()

    platforms = [
        ("kijiji", kijiji.scrape),
        ("autotrader", autotrader.scrape),
        ("rentfaster", rentfaster.scrape),
        ("used_ca", used_ca.scrape),
        ("realtor", realtor.scrape),
        ("zillow", zillow.scrape),
        ("ebay", ebay.scrape),
    ]

    for platform_name, scraper_fn in platforms:
        print(f"[INFO] Running scraper for: {platform_name}")

        try:
            raw_listings = scraper_fn()
            mark_success(platform_name)
        except Exception as e:
            print(f"[ERROR] Scraper failed for {platform_name}: {e}")
            mark_failure(platform_name, str(e))
            continue

        for raw in raw_listings:
            try:
                listing = normalize_listing(raw, platform_name)
                listing = categorize_listing(listing)
                listing = score_listing(listing)
                listing = infer_demographics(listing)

                if is_spam(listing):
                    continue

                col.insert_one(listing)

            except Exception as e:
                print(f"[ERROR] Processing failed for {platform_name}: {e}")
                continue


if __name__ == "__main__":
    run_all()
