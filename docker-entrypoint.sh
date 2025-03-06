#!/bin/sh

set -o allexport
set -o nounset
set -o errexit
set -o xtrace

# Collect static files
python manage.py collectstatic --noinput

# debug info
pwd
echo "DJANGO_SETTINGS_MODULE is set to: $DJANGO_SETTINGS_MODULE"

# Check environment and run appropriate command. increased verbosity b/c of lack of messages when there are problems after "Watching for file changes with StatReloader"
if [ "$DJANGO_SETTINGS_MODULE" = "config.settings.local" ]; then
    # Local development
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000 --verbosity 3
else
    # Production
    exec gunicorn config.wsgi:application \
      --workers 3 \
      --bind 0.0.0.0:8000 \
      "$@"
fi
