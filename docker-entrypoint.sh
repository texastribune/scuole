#!/bin/sh

# Run app
exec gunicorn config.wsgi:application \
  --workers 3 \
  --bind 0.0.0.0:8000 \
  "$@"
