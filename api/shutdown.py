# f1ndr_backend/api/shutdown.py

async def on_shutdown():
    """
    Shutdown hook for cleanup tasks.
    Add cleanup logic here (closing DB connections, stopping workers, etc.)
    """
    print("f1ndr backend is shutting down...")
