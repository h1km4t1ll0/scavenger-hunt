#!/bin/bash

sleep 10
psql postgresql://postgres:postgres@database -f psql.sql

service nginx start
python3 manage.py collectstatic --noinput
sleep 1
python3 manage.py makemigrations
sleep 1
python3 manage.py migrate
sleep 1
python3 manage.py initadmin
sleep 1
/bin/gunicorn3 wsgi:application -b 127.0.0.1:8000 --env DJANGO_SETTINGS_MODULE=scavengerHunt.settings --user www-data --group www-data
