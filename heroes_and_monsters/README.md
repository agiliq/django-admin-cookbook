## Running the project locally

You should follow these steps to run the project locally.

### Create a virtual environment

You should create a virtual environment, preferably with Python 3.6

If you use **virtualenvwrapper**, you could do:

    mkvirtualenv --python=/usr/local/bin/python3 django-admin-cookbook

### Install the requirements

    pip install -r requirements.txt

### Run migrations

    python manage.py migrate

### Run server and access admin

    python manage.py runserver

You can access admins at:

    http://localhost:8000/entity-admin

    http://localhost:8000/event-admin
