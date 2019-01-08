#!/usr/bin/env bash

sleep 10
python manage.py collectstatic --no-input
python manage.py migrate
uwsgi --ini uwsgi.ini
