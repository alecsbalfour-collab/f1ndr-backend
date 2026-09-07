# f1ndr_backend/api/startup.py

async def on_startup():
    """
    Startup hook for initializing resources, connections, or background tasks.
    Reconstructed because the original api/main.py depended on this.
    Add your database connections or initialization logic here.
    """
    print("F1NDR backend is starting up...")

async def on_shutdown():
    """
    Shutdown hook for cleanup tasks.
    """
    print("F1NDR backend is shutting down...")
