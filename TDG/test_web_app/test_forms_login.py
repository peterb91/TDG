from TDG.web_app.forms_login import LoginForm, RegisterForm, ValidationError, allowed_characters_check
from flask import Flask
import pytest

app = Flask(__name__)
app.testing = True
app.config['WTF_CSRF_ENABLED'] = False


class MockField:
    pass


def test_allowed_characters_check_empty_field():
    MockField.data = ''
    with pytest.raises(ValidationError):
        allowed_characters_check('_', MockField)


def test_allowed_characters_check_correct():
    MockField.data = 'Tester123!@#$'
    assert allowed_characters_check('', MockField) is None


def test_login_and_password_both_fields_empty():
    with app.test_client() as c:
        c.post(data={'login': '', 'password': ''})
        form = LoginForm()
        assert form.validate_on_submit() is False


def test_login_and_password_correct():
    with app.test_client() as c:
        c.post(data={'login': 'tester', 'password': 'tester'})
        form = LoginForm()
        assert form.validate_on_submit() is True


def test_register_correct():
    with app.test_client() as c:
        c.post(data={'login': 'tester', 'password': 'qwerty', 'email': 'tester@o2.pl', 'confirm_password': 'qwerty'})
        form = RegisterForm()
        assert form.validate_on_submit() is True
