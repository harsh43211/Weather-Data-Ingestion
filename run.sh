#!/bin/bash

# create virtual environment
python3 -m venv env

# activate environment
source env/bin/activate

# install requirements
pip install -r requirements.txt

# migrate database
python3 src/manage.py makemigrations
python3 src/manage.py migrate

# ingest data
python3 ingest.py

# run server
python3 src/manage.py runserver
