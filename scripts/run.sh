# !/bin/sh

set -e

gunicorn file_storage.wsgi --bind 0.0.0.0:$PORT