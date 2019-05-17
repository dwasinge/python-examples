# Django REST Framework Simple JWT Auth Service

Service provides JWT tokens for registered users.  Provides an API to get access token, refresh token, and verify token.

## Run locally

Clone the Repository:

```bash
git clone https://github.com/dwasinge/python-examples.git
```
### Setup Virtual Environment

```bash

# change to project directory
cd django_rest_framework_jwt_service

# use pipenv to create venv
pipenv shell

# install all modules to the venv
pipenv sync

```
## Create user for testing

```bash
# Create user and follow prompts for input
python manage.py createsuperuser
```

## Apply Simple JWT Migrations

```bash
python manage.py migrate
```
## Run the Development server

```bash
python manage.py runserver
```

## Available endpoints

http://localhost:8000/api/token/

```bash

  curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "yourusername", "password": "youruserpassword"}' \
    http://localhost:8000/api/token/

```

http://localhost:8000/api/token/refresh/

```bash


  curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"refresh":"tokentorefrest"}' \
    http://localhost:8000/api/token/refresh/

```

http://localhost:8000/api/token/verify/

TODO