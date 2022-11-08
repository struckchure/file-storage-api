# !/bin/sh

set -e

python manage.py runserver 0.0.0.0:$PORT
