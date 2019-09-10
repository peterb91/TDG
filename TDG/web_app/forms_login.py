"""
Forms for validating login page and registration page fields.
"""

from string import ascii_letters, digits

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField

ALLOWED_CHARS = '!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~' + ascii_letters + digits

USERNAME_DESCR = 'Username'
PASSWORD_DESCR = 'New Password'
REMEMBER_DESCR = 'Remember me'
EMAIL_DESCR = 'Email Address'
CONFIRM_DESCR = 'Repeat Password'


def allowed_characters_check(form, field):
    """
    Custom validator for characters allowed in login and password
    """
    allowed_characters_set = set(ALLOWED_CHARS)
    form_characters_set = set(field.data)
    if not form_characters_set.issubset(allowed_characters_set) or not bool(field.data):
        raise ValidationError('Not allowed character')


class LoginForm(FlaskForm):
    """
    """
    login = StringField(USERNAME_DESCR, validators=[InputRequired(), Length(min=4, max=15), allowed_characters_check])
    password = PasswordField(PASSWORD_DESCR, validators=[InputRequired(), Length(min=6, max=15), allowed_characters_check])


class RegisterForm(LoginForm):
    """
    """
    email = EmailField(EMAIL_DESCR, validators=[InputRequired(), Email(), Length(max=120)])
    confirm_password = PasswordField(CONFIRM_DESCR, validators=[InputRequired(), EqualTo(fieldname='password'), allowed_characters_check])
