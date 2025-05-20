#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Create static directories if they don't exist
mkdir -p static
mkdir -p blog/static/blog

# Run collectstatic with clear flag to ensure all files are collected
python manage.py collectstatic --noinput --clear

# Run migrations
python manage.py migrate