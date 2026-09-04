def apply_validate_rules(payload, rules):
    out = {"valid": True, "errors": []}

    if rules.get("check_title") and not payload.get("title"):
        out["valid"] = False
        out["errors"].append("Missing title")

    if rules.get("check_price") and not payload.get("price"):
        out["valid"] = False
        out["errors"].append("Missing price")

    if rules.get("check_location") and not payload.get("location"):
        out["valid"] = False
        out["errors"].append("Missing location")

    return out
