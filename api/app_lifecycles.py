from startup import on_startup
from shutdown import on_shutdown

def register_lifecycle(app):
    """
    Attach startup and shutdown events to the FastAPI app.
    """
    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)
