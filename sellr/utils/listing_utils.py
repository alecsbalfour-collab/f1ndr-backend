def apply_listing_rules(payload, rules):
    out = payload.copy()

    if rules.get("strip_whitespace"):
        out = {k: str(v).strip() if isinstance(v, str) else v for k, v in out.items()}

    if rules.get("require_title") and not out.get("title"):
        out["title"] = "Untitled"

    if rules.get("require_price") and not out.get("price"):
        out["price"] = "0"

    out["status"] = rules.get("default_status", "active")
    return out
