#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

cd together_project
# run Celery worker for our project together_project with Celery configuration stored in Celeryconf
su -m myuser -c "celery worker -A together_project.celeryconf -Q default -n default@%h"
