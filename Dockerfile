FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install ADK
RUN pip install --no-cache-dir google-adk

# Copy the entire project
COPY . .

# Expose the default ADK web port
EXPOSE 8000

# Set environment variable for Google API key (will be provided at runtime)
ENV GOOGLE_API_KEY=""

# Run ADK web from the parent directory as required
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]