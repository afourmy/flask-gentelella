from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

## login and registration


class LoginForm(FlaskForm):
    username = StringField('Username', id='username_login')
    password = PasswordField('Password', id='pwd_login')


class CreateAccountForm(FlaskForm):
    username = StringField('Username', id='username_create')
    email = StringField('Email')
    password = PasswordField('Password', id='pwd_create')
