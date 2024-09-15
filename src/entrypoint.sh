#!/bin/sh

set -e

if [ "$1" = "app" ]; then
    echo "Collecting static files"
    poetry run python manage.py collectstatic --clear --noinput

    echo "Running migrations"
    poetry run python manage.py migrate

    echo "Running in production mode"
    exec poetry run gunicorn -c gunicorn.conf.py
else
    exec "$@"
fi
