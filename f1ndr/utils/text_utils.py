def clean_text(value):
    """
    Clean text fields from scrapers.
    """
    if not value:
        return ""
    return str(value).replace("\n", " ").replace("\t", " ").strip()


def extract_price(text):
    """
    Convert price strings like '$1,200' → 1200.0
    """
    if not text:
        return 0.0

    cleaned = (
        text.replace("$", "")
            .replace(",", "")
            .replace("CAD", "")
            .strip()
    )

    try:
        return float(cleaned)
    except:
        return 0.0
