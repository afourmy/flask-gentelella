from app.home import blueprint
from flask import render_template
from flask_login import login_required


@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html')


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')
