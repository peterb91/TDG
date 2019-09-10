from TDG.web_app.model_control import *
import pytest

app.testing = True
app = app.test_client()
data = {}
app.post('/', data={'ratio': '50',
                    'records_no': '1000',
                    'txt': '',
                    'headers': 'y_headers',
                    'login_min_length': '1',
                    'login_max_length': '50',
                    'login_special_char': 'login_all_special',
                    'login_textarea_custom': '',
                    'pass_min_length': '1',
                    'pass_max_length': '50',
                    'pass_special_char': 'pass_all_special',
                    'pass_textarea_custom': ''})


@pytest.mark.skip
def test_login_data():
    needed = ['login_or_password', 'min_length', 'max_length', 'positive_percentage', 'list_length']
    login_d = {x: data[x] for x in needed}
    assert (login_data() == login_d)


@pytest.mark.skip
def test_pass_data():
    needed = ['min_length', 'max_length']
    pass_d = {x: data[x] for x in needed}
    assert (pass_data() == pass_d)


@pytest.mark.skip
def test_format():
    assert (formating() == 'txt')


@pytest.mark.skip
def test_login_specials():
    assert (login_specials() == '`~!@#$%^&*()_+-=[]{}|\;\':\",<.>/?')


@pytest.mark.skip
def test_pass_specials():
    assert (pass_specials() == '`~!@#$%^&*()_+-=[]{}|\;\':\",<.>/?')


@pytest.mark.skip
def test_headers():
    assert (headers() is True)
