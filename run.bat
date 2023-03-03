@echo off

:: create virtual environment
pip install virtualenv
virtualenv env

:: activate environment
env\Scripts\activate

:: install requirements
pip install -r requirements.txt

:: migrate database
python src\manage.py makemigrations
python src\manage.py migrate

:: ingest data
python ingest.py

:: run server
python src\manage.py runserver
