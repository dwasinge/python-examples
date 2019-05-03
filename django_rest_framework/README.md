# Overview

This is a simple RESTful API that manages people.  Each person has a first name, last name, and age.  People can be created, retrieved, updated, and deleted using the API methods.

---

# How do I use it?

## Prerequistes

* python is installed
* pip is installed
* use pip to install pipenv
```
pip install pipenv
```

## Clone the repository

```
git clone git@github.com:dwasinge/python-examples.git
```

## Create a virtual environment using the Pipfile

```
cd django_rest_framework
pipenv install
```

## Start VENV Shell

```
pipenv shell
```

## Run locally

### Start Dev Server

```
python manage.py runserver
```

### Test API

The server starts on http://localhost:8000 by default.

#### List Endpoints

* POST /people
  * creates a new person resource
* GET /people
  * returns a list of all people resources

#### Single Resource Endpoints

* GET /people/{id}
  * retrieves the person resource with the given id, returns 404 otherwise
* PUT /people/{id}
  * updates the person resource with the given id, returns 404 otherwise
* DELETE /people/{id}
  * deletes the person resource with the given id, returns 404 otherwise
