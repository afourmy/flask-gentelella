from flask import Blueprint, render_template, redirect, url_for

blueprint = Blueprint(
    'base_blueprint', 
    __name__, 
    url_prefix = '', 
    template_folder = 'templates',
    static_folder = 'static'
    )

@blueprint.route('/')
def route_default():
    return redirect(url_for('home_blueprint.index'))

@blueprint.route('/<template>')
def route_template(template):
    return render_template(template + '.html')

@blueprint.route('/fixed_<template>')
def route_fixed_template(template):
    return render_template('fixed/fixed_{}.html'.format(template))

@blueprint.route('/page_<error>')
def route_errors(error):
    return render_template('errors/page_{}.html'.format(error))

## Login & Registration

@blueprint.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'GET':
        form = CreateAccountForm(request.form)
        return render_template('login/create_account.html', form=form)
    else:
        login_form = LoginForm(request.form)
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users_blueprint.login'))

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = str(request.form['username'])
        password = str(request.form['password'])
        user = db.session.query(User).filter_by(username=username).first()
        if user and password == user.password:
            flask_login.login_user(user)
            return redirect(url_for('base_blueprint.dashboard'))
        return render_template('errors/page_403.html')
    if not flask_login.current_user.is_authenticated:
        form = LoginForm(request.form)
        return render_template('login/login.html', form=form)
    return redirect(url_for('base_blueprint.dashboard'))

@blueprint.route('/logout')
def logout():
    flask_login.logout_user()
    return render_template('login/login.html', form=form)

## Errors

@blueprint.errorhandler(403)
def not_found_error(error):
    return render_template('errors/page_403.html'), 403

@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404

@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500