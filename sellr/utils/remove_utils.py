def apply_remove_rules(payload, rules):
    out = payload.copy()

    if rules.get("mark_removed"):
        out["status"] = "removed"

    return out
