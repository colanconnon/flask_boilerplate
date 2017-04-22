#!/bin/bash
python3 manage.py db upgrade
if [ "$FLASK_ENV" == "development" ]
then
        python wsgi.py
else
       /usr/local/bin/gunicorn wsgi -w 2 -b :8000 --worker-class=meinheld.gmeinheld.MeinheldWorker --reload;
fi