#!/bin/sh

set -o allexport
set -o nounset
set -o errexit
set -o xtrace

# Collect static files
python manage.py collectstatic --noinput

# Run app
python manage.py runserver