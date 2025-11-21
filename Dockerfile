FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files and copy media files
RUN python manage.py collectstatic --noinput && \
    python manage.py copy_media_to_static

# Expose port
EXPOSE 8000

# Run migrations and start server
CMD python manage.py migrate && gunicorn ecommerce_project.wsgi:application --bind 0.0.0.0:$PORT
