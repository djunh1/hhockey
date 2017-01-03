#!/bin/bash

NAME="hhockey"
DJANGODIR=/home/ec2-user/sites/staging-hopewellhockey.com/source
SOCKFILE=/tmp/staging-hopewellhockey.com.socket
USER=ec2-user
GROUP=webapps
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=hhockey.settings.override
DJANGO_WSGI_MODULE=hhockey.wsgi


# Activate the virtual environment
cd $DJANGODIR
source ../virtualenv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH


# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../virtualenv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER  \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
--log-file=-