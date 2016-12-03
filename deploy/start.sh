#!/bin/sh
python3 manage.py db upgrade
if [ "$FLASK_ENV" == "development" ]; then
        python app.py
else
       /usr/local/bin/gunicorn wsgi -w 2 -b :8000 --reload;
fi