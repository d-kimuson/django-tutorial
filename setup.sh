#!/bin/bash

# RUN: source setup.sh

cd django-tutorial
python -m venv env && source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations && python manage.py migrate
python manage.py loaddata fixture.json
