#!/bin/bash

# create virtual environment
pip3 install virtualenv
virtualenv env

# activate environment
source env/bin/activate

# install requirements
pip3 install -r requirements.txt

# migrate database
python3 src/manage.py makemigrations
python3 src/manage.py migrate

# ingest data
python3 ingest.py

# run server
python3 src/manage.py runserver
