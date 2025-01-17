#!/bin/bash

# install dependencies
pip install setuptools
pip install -r requirements.txt

# run django comment
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic