#!/usr/bin/env bash
# start-server.sh

# if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
#     (cd main; python manage.py createsuperuser --no-input)
# fi
# if [-n "$DEV_MODE" ]; then
#     (python manage.py migrate; python manage.py makemigrations)
# fi

(cd main; ls; gunicorn main.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"