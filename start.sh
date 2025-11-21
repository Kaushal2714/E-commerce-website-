#!/bin/bash

# Exit on error
set -e

echo "Starting deployment..."

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Copy media files to static
echo "Copying media files..."
python manage.py copy_media_to_static

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn ecommerce_project.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info
