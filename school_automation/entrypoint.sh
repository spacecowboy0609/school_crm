#!/bin/sh

while ! mysqladmin ping -h"mysql" --silent; do
    echo "Waiting for MySQL..."
    sleep 2
done
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

exec "$@"
