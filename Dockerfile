FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Create logs directory for logging output
RUN mkdir -p /app/logs

# Install dependencies (including Prometheus integration)
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Start the FastAPI app with Uvicorn
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
