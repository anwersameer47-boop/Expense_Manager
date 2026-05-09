#!/bin/bash
# Startup script for Expense Tracker Django App

set -e

cd "$(dirname "$0")"

# Install Django if not already present (use --break-system-packages for Nix/Replit)
echo ">>> Checking dependencies..."
python3 -c "import django" 2>/dev/null || python3 -m pip install -r requirements.txt --quiet --break-system-packages

# Run database migrations (safe to run multiple times)
echo ">>> Running database migrations..."
python3 manage.py migrate --run-syncdb

# Start the Django development server
PORT="${PORT:-8000}"
echo ">>> Starting Django server on port $PORT..."
exec python3 manage.py runserver "0.0.0.0:$PORT"
