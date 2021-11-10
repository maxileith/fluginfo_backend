#!/bin/sh
python manage.py makemigrations &&
python manage.py migrate &&

gunicorn fluginfo.wsgi:application --bind=0.0.0.0:80
