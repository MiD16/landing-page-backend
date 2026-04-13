#!/bin/bash

# Exit on error
set -e

echo "Starting Django application on Render..."

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist (optional, for production you might skip this)
echo "Creating superuser if not exists..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser created successfully!')
else:
    print('Superuser already exists.')
" || echo "Superuser creation skipped"

# Get the port from Render's environment variable or default to 8000
PORT=${PORT:-10000}

echo "Starting Gunicorn server on port $PORT..."
exec gunicorn company_landing_page_backend.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120
