[![Build Status](https://travis-ci.org/afourmy/flask-gentelella.svg?branch=master)](https://travis-ci.org/afourmy/flask-gentelella)
[![Coverage Status](https://coveralls.io/repos/github/afourmy/flask-gentelella/badge.svg?branch=master)](https://coveralls.io/github/afourmy/flask-gentelella?branch=develop)

# Flask Gentelella

[Gentelella](https://github.com/puikinsh/gentelella) is a free to use Bootstrap admin template.

This project integrates Gentelella with Flask using blueprints, flask_login and flask_migrate. It is also available on [Dockerhub](https://hub.docker.com/r/afourmy/flask-gentelella/) for the application to run in a docker container (see below).

![Gentelella Bootstrap Admin Template](https://cdn.colorlib.com/wp/wp-content/uploads/sites/2/gentelella-admin-template-preview.jpg "Gentelella Theme Browser Preview")

**[Template Demo](https://colorlib.com/polygon/gentelella/index.html)**

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
