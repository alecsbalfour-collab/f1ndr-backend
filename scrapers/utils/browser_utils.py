def launch_browser():
    return {"browser": "mock", "status": "running"}

def close_browser(browser: dict):
    browser["status"] = "closed"
    return browser
