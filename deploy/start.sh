#!/bin/bash
python3 manage.py db upgrade
cd /src/
/usr/local/bin/gunicorn myapp.wsgi -w 8 -b :8000 --worker-class=meinheld.gmeinheld.MeinheldWorker --reload;
