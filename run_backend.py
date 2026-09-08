import uvicorn
from api.main import app  # <-- Exposes the app object to Render's root search process

if __name__ == "__main__":
    uvicorn.run(
        "run_backend:app",  # Change this to point right here to the root file string
        host="127.0.0.1", 
        port=8000, 
        reload=True
    )
