import uvicorn
from api.main import app

if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",  # or just app
        host="0.0.0.0",
        port=8000,
        reload=True
    )
