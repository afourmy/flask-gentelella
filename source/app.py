from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from inspect import stack
from logging import Formatter, FileHandler
from os.path import abspath, dirname, join
import logging
import os
import sys

# prevent python from writing *.pyc files / __pycache__ folders
sys.dont_write_bytecode = True

path_app = dirname(abspath(stack()[0][1]))
if path_app not in sys.path:
    sys.path.append(path_app)

path_source = os.path.dirname(os.path.abspath(__file__))

from database import db, create_database
from base.routes import login_manager
from base.models import User

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    for module_name in ('forms', 'ui', 'home', 'tables', 'data', 'additional', 'base'):
        module = import_module('{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def configure_login_manager(app, User):
    @login_manager.user_loader
    def user_loader(id):
        return db.session.query(User).filter_by(id=id).first()
    
    @login_manager.request_loader
    def request_loader(request):
        username = request.form.get('username')
        user = db.session.query(User).filter_by(username=username).first()
        return user if user else None

def configure_database(app):
    create_database()
    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def configure_logs(app):
    if not app.debug:
        logging.basicConfig(filename='error.log',level=logging.DEBUG)
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())

def create_app(config='config'):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object('config')
    
    register_extensions(app)
    register_blueprints(app)
    
    from base.models import User
    configure_login_manager(app, User)
    
    configure_database(app)
    configure_logs(app)

    return app

app = create_app()

## Tear down SQLAlchemy 

@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()

## Route to any template

# @app.route('/')
# def index():
#     return render_template('index.html')
# 
# @app.route('/<template>')
# def route_template(template):
#     return render_template(template)

## Logs

if not app.debug:
    file_handler = FileHandler('error.log')
    format = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    file_handler.setFormatter(Formatter(format))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = int(os.environ.get('PORT', 5000)),
        threaded = True
        )
