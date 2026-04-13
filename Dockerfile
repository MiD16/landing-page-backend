# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project
COPY . /app/

# Make entrypoints executable
RUN chmod +x /app/entrypoint.sh /app/render-entrypoint.sh

# Expose port (Render uses $PORT environment variable, typically 10000)
EXPOSE 8000

# Use render-specific entrypoint for Render.com deployment
# You can change this back to entrypoint.sh for local development
ENTRYPOINT ["bash", "/app/render-entrypoint.sh"]
