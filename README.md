 # Weather API with Django
 This is a Django-based Weather API that provides weather data to users. It includes instructions on how to set up a virtual environment, install the required dependencies, run migrations, and ingest data. Additionally, it offers information on how to access and use the API.

The API endpoints provide access to the following functionalities:

    /api/weather - retrieves weather data
    /api/weather/stats - provides statistics about the data
    /api/schema/swagger-ui/ - Swagger UI that provides an overview of the API's capabilities.

## Prerequisites

The following prerequisites are required to use this API:

    Python (3.7 or higher)
    Virtualenv
    SQLite (or PostgreSQL if deploying to AWS)
    AWS account (if deploying to AWS)

## Installation and Usage

### Automatic Installation:

    ./run.sh (in Linux and Mac)
    ./run.bat (in Windows)

### Manual Installation:
### To install the required dependencies, create and activate a virtual environment with the following commands:

    pip install virtualenv
    virtualenv env

### To activate the virtual environment:

    env/Scripts/activate (in Windows)
    source env/bin/activate (in Linux and Mac)

### Then, install the required dependencies:

    pip install -r requirements.txt

### To run migrations:


    python3 src/manage.py makemigrations
    python3 src/manage.py migrate

### To ingest the data:

    python3 ingest.py

### To run the server:

    python3 src/manage.py runserver

### To access the API endpoints, use the following links:

    http://127.0.0.1:8000/api/weather
    http://127.0.0.1:8000/api/weather/stats
    http://127.0.0.1:8000/api/schema/swagger-ui/

## To run tests:

    cd src
    python manage.py test

# AWS Deployment

To deploy the API to AWS, use the following steps:

    - Deploy Django API with AWS EC2
    - Deploy the database with Amazon Relational Database Service (RDS)
    - Store data with AWS S3
    - Schedule data ingestion with AWS EC2 and create a cron job.
    - Store ingested data in the RDS database.

## Conclusion
    - This approach provides a scalable, secure, and easily managed deployment of the Django API, database, and data ingestion code
    - The load balancer and auto-scaling can be used, AWS EC2 and Amazon RDS ensure that the API and database can handle changing levels of traffic.
