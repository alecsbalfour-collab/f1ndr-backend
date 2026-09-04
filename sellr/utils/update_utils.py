def apply_update_rules(payload, rules):
    out = payload.copy()

    if rules.get("strip_whitespace"):
        out = {k: str(v).strip() if isinstance(v, str) else v for k, v in out.items()}

    return out
