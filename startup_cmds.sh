#!/bin/bash

python3 manage.py migrate
python3 manage.py shell < init-script.py
python3 manage.py runserver 0.0.0.0:8000
