from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from logging import Formatter, FileHandler
import logging
import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

path_source = os.path.dirname(os.path.abspath(__file__))
for module_name in ('forms', 'UI_elements', 'home', 'tables', 'data_presentation', 'additional', 'base'):
    module = import_module('{}.routes'.format(module_name))
    app.register_blueprint(module.blueprint)

## Tear down SQLAlchemy 

@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()

## Route to any template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<template>')
def route_template(template):
    return render_template(template)

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
    # run on port 5000 by default
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
