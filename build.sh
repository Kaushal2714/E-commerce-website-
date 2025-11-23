#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Load initial data (categories and products)
python manage.py loaddata fixtures/initial_data.json || echo "Fixtures already loaded or error occurred"

# Create default superuser if none exists
python manage.py create_default_superuser