chmod +x start.sh
#!/bin/bash

# Load environment variables
export $(grep -v '^#' .env | xargs)

# Default port fallback
PORT=${PORT:-8000}

echo "Starting F1NDR Backend on port $PORT..."

# Run FastAPI with Uvicorn
uvicorn main:app --host 0.0.0.0 --port $PORT --reload
