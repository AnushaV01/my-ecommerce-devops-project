# Use official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Add a non-root user (optional, secure)
RUN useradd -m appuser
USER appuser

# Expose the port (from .env: 5050)
EXPOSE 5050

# Run the app
CMD ["python", "main.py"]
