# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies (fixes libGL issue)
RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker caching
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full backend app
COPY backend/ .

# Expose port
EXPOSE 8000

# Start FastAPI using Uvicorn (For Railway)
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Render-compatible dynamic port binding
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]