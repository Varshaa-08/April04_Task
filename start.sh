# start.sh (Startup Script for Backend Only)
#!/bin/bash
echo "Starting FastAPI Backend..."
uvicorn backend:app --host 0.0.0.0 --port 8000
