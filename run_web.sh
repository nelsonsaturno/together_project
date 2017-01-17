#!/bin/sh

# wait for PSQL server to start
sleep 10

cd together_project
# prepare init migration
su -m myuser -c "python manage.py makemigrations together_project"
# migrate db, so we have the latest db schema
su -m myuser -c "python manage.py migrate"
# start development server on public ip interface, on port 8000
su -m myuser -c "python manage.py runserver localhost:8000"
