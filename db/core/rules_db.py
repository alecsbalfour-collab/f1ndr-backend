def apply_db_rules(settings: dict):
    """
    Apply database rules or transformations to the DB settings.
    This keeps DB logic consistent with your architecture.
    """

    # Ensure port is an integer
    settings["db_port"] = int(settings.get("db_port", 27017))

    # Normalize host
    if "db_host" in settings and isinstance(settings["db_host"], str):
        settings["db_host"] = settings["db_host"].lower()

    # Ensure database name exists
    if not settings.get("db_name"):
        settings["db_name"] = "f1ndr"

    return settings
