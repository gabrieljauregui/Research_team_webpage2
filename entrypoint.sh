#!/bin/sh

# wait for PSQL server to start
sleep 10

# run Django migrations
python manage.py migrate

# start development server
python manage.py runserver 0.0.0.0:8000
