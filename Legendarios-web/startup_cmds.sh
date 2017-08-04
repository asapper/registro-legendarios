#!/bin/bash

python manage.py migrate
python manage.py shell < init-script.py
python manage.py runserver 0.0.0.0:8000
