[![Build Status](https://travis-ci.org/afourmy/flask-gentelella.svg?branch=master)](https://travis-ci.org/afourmy/flask-gentelella)
[![Coverage Status](https://coveralls.io/repos/github/afourmy/flask-gentelella/badge.svg?branch=master)](https://coveralls.io/github/afourmy/flask-gentelella?branch=develop)

# Flask Gentelella

[Gentelella](https://github.com/puikinsh/gentelella) is a free to use Bootstrap admin template.

This project integrates Gentelella with Flask using: 
    - [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/) for scalability.
    - [flask_login](https://flask-login.readthedocs.io/en/latest/) to implement a real login system.
    - [flask_migrate](https://flask-migrate.readthedocs.io/en/latest/).

Flask-gentelella also comes with a robust CI/CD pipeline using:
    - The [Pytest](https://docs.pytest.org/en/latest/) framework for the test suite (see the `tests` folder).
    - [Travis CI](https://travis-ci.org/afourmy/flask-gentelella)
    - [Coverage](https://coveralls.io/github/afourmy/flask-gentelella) to measure the code coverage of the tests.
    - [Selenium](https://www.seleniumhq.org/) to test the application with headless chromium.
    - A Dockerfile showing how to containerize the application with gunicorn, and a [Docker image](https://hub.docker.com/r/afourmy/flask-gentelella/) available on dockerhub, and integrated to the CI/CD pipeline (see instructions below).

# Installation

### (Optional) Set up a [virtual environment](https://docs.python.org/3/library/venv.html) 

### 1. Get the code
    git clone https://github.com/afourmy/flask-gentelella.git
    cd flask-gentelella

### 2. Install requirements 
    pip install -r requirements.txt

### 3. Run the code
    cd source
    python app.py

### 4. Go the http://127.0.0.1:5000/

### 5. Create an account and log in

# Run Flask Gentelella in a docker container

### 1. Fetch the image on dockerhub
    docker pull afourmy/flask-gentelella

### 2. Find the name of the docker image
    docker images

### 3. Run the image on port 5000
    docker run -p 5000:5000 image_name
