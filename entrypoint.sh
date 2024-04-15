#!/bin/bash

#sleep 10
psql postgresql://postgres:postgres@database -f psql.sql
python3 manage.py collectstatic --noinput
#sleep 1
python3 manage.py makemigrations
#sleep 1
python3 manage.py migrate
#sleep 1
python3 manage.py initadmin
#sleep 1
gunicorn wsgi:application -b 127.0.0.1:8000 --env DJANGO_SETTINGS_MODULE=shelbyBot.settings
#--user www-data --group www-data
