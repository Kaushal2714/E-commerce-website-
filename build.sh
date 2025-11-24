#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Load sample products
python manage.py load_sample_products

# Create default superuser if none exists
python manage.py create_default_superuser