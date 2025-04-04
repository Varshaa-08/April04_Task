# start.sh (Startup Script for Backend Only)
#!/bin/bash
echo "Starting FastAPI Backend..."
nohup gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend:app --bind 0.0.0.0:8000 &