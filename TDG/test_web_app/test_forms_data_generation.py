from TDG.web_app.forms_data_generation import SameForm, DifferentForm
from flask import Flask
import pytest

app = Flask(__name__)
app.testing = True
app.config['WTF_CSRF_ENABLED'] = False


def test_correct_single_form_passes():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-12",
            "headers": "y_headers",
            "login_max_length": "12",
            "login_min_length": "4",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "ratio": "43",
            "records_no": "100",
            "same_form": "same_form",
            "txt": ""})
        form = SameForm()
        assert form.validate_on_submit() is True


@pytest.mark.parametrize("login_len, expected", [
    ('0', False),
    ('1', True),
    ('50', True),
    ('51', False),
])
def test_login_len_boundary_values(login_len, expected):
    with app.test_client() as c:
        c.post(data={
            "amount": "1-12",
            "headers": "y_headers",
            "login_max_length": login_len,
            "login_min_length": login_len,
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "ratio": "43",
            "records_no": "100",
            "same_form": "same_form",
            "txt": ""})
        form = SameForm()
        assert form.validate_on_submit() == expected


def test_login_len_not_decimal():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-12",
            "headers": "y_headers",
            "login_max_length": "a",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "ratio": "43",
            "records_no": "100",
            "same_form": "same_form",
            "txt": ""})
        form = SameForm()
        assert form.validate_on_submit() is False


def test_login_len_not_integer():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-12",
            "headers": "y_headers",
            "login_max_length": "4.5",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "ratio": "43",
            "records_no": "100",
            "same_form": "same_form",
            "txt": ""})
        form = SameForm()
        assert form.validate_on_submit() is False


def test_login_len_is_required():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-12",
            "headers": "y_headers",
            "login_max_length": "",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "ratio": "43",
            "records_no": "100",
            "same_form": "same_form",
            "txt": ""})
        form = SameForm()
        x = form.validate_on_submit()
        for fieldname, value in form.errors.items():
            assert 'login_max_length' in fieldname
            assert "This field is required." in value


def test_correct_different_form_passes():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-27",
            "amountPas": "1-26",
            "different_form": "different_form",
            "headers": "y_headers",
            "import_btn": "",
            "login_max_length": "6",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "pass_max_length": "26",
            "pass_min_length": "10",
            "pass_special_char": "pass_custom_special",
            "pass_textarea_custom": "*&^",
            "ratio": "70",
            "records_no": "20",
            "txt": ""
        })
        form = DifferentForm()
        assert form.validate_on_submit() is True


@pytest.mark.parametrize("pass_len, expected", [
    ('0', False),
    ('1', True),
    ('50', True),
    ('51', False),
])
def test_password_len_boundary_values(pass_len, expected):
    with app.test_client() as c:
        c.post(data={
            "amount": "1-27",
            "amountPas": "1-26",
            "different_form": "different_form",
            "headers": "y_headers",
            "import_btn": "",
            "login_max_length": "6",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "pass_max_length": pass_len,
            "pass_min_length": pass_len,
            "pass_special_char": "pass_custom_special",
            "pass_textarea_custom": "*&^",
            "ratio": "70",
            "records_no": "20",
            "txt": ""
        })
        form = DifferentForm()
        x = form.validate_on_submit()
        print('\n===DATA===')
        for fieldname, value in form.data.items():
            print("** {} = {!r}".format(fieldname, value))
        print('\n===ERRORS===')
        for fieldname, value in form.errors.items():
            print("** {} = {!r}".format(fieldname, value))

        assert form.validate_on_submit() == expected


def test_password_len_not_decimal():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-27",
            "amountPas": "1-26",
            "different_form": "different_form",
            "headers": "y_headers",
            "import_btn": "",
            "login_max_length": "5",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "pass_max_length": "pppppppppppppppppppp",
            "pass_min_length": "1",
            "pass_special_char": "pass_custom_special",
            "pass_textarea_custom": "*&^",
            "ratio": "70",
            "records_no": "20",
            "txt": ""
        })
        form = DifferentForm()
        x = form.validate_on_submit()
        for fieldname, value in form.errors.items():
            assert 'pass_max_length' in fieldname
            assert "This field is required." in value


def test_password_len_not_integer():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-27",
            "amountPas": "1-26",
            "different_form": "different_form",
            "headers": "y_headers",
            "import_btn": "",
            "login_max_length": "5",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "pass_max_length": "4.543535423323",
            "pass_min_length": "1",
            "pass_special_char": "pass_custom_special",
            "pass_textarea_custom": "*&^",
            "ratio": "70",
            "records_no": "20",
            "txt": ""
        })
        form = DifferentForm()
        x = form.validate_on_submit()
        for fieldname, value in form.errors.items():
            assert 'pass_max_length' in fieldname
            assert "This field is required." in value


def test_password_len_is_required():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-27",
            "amountPas": "1-26",
            "different_form": "different_form",
            "headers": "y_headers",
            "import_btn": "",
            "login_max_length": "5",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "pass_max_length": "",
            "pass_min_length": "1",
            "pass_special_char": "pass_custom_special",
            "pass_textarea_custom": "*&^",
            "ratio": "70",
            "records_no": "20",
            "txt": ""
        })
        form = DifferentForm()
        x = form.validate_on_submit()
        for fieldname, value in form.errors.items():
            assert 'pass_max_length' in fieldname
            assert "This field is required." in value


def test_password_special_is_required():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-27",
            "amountPas": "1-26",
            "different_form": "different_form",
            "headers": "y_headers",
            "import_btn": "",
            "login_max_length": "5",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "pass_max_length": "9",
            "pass_min_length": "1",
            "pass_special_char": "",
            "pass_textarea_custom": "*&^",
            "ratio": "70",
            "records_no": "20",
            "txt": ""
        })
        form = DifferentForm()
        x = form.validate_on_submit()
        for fieldname, value in form.errors.items():
            assert 'pass_special_char' in fieldname
            assert "This field is required." in value


@pytest.mark.parametrize("ratio, expected", [
        ('0', False),
        ('1', True),
        ('100', True),
        ('101', False),
    ])
def test_ratio_boundary_values(ratio, expected):
    with app.test_client() as c:
        c.post(data={
            "amount": "1-27",
            "amountPas": "1-26",
            "different_form": "different_form",
            "headers": "y_headers",
            "import_btn": "",
            "login_max_length": "10",
            "login_min_length": "1",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "pass_max_length": "26",
            "pass_min_length": "1",
            "pass_special_char": "pass_custom_special",
            "pass_textarea_custom": "*&^",
            "ratio": ratio,
            "records_no": "20",
            "txt": ""
            })
        form = DifferentForm()
        assert form.validate_on_submit() == expected


def test_ratio_not_decimal():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-12",
            "headers": "y_headers",
            "login_max_length": "1",
            "login_min_length": "9",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": "!@# ",
            "ratio": "nxsiduxaon",
            "records_no": "100",
            "same_form": "same_form",
            "txt": ""})
        form = SameForm()
        x = form.validate_on_submit()
        for fieldname, value in form.errors.items():
            assert 'ratio' in fieldname
            assert "This field is required." in value


def test_ratio_not_integer():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-12",
            "headers": "y_headers",
            "login_max_length": "1",
            "login_min_length": "9",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "ratio": "1.3",
            "records_no": "100",
            "same_form": "same_form",
            "txt": ""})
        form = SameForm()
        x = form.validate_on_submit()
        for fieldname, value in form.errors.items():
            assert 'ratio' in fieldname
            assert "This field is required." in value


def test_ratio_is_required():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-12",
            "headers": "y_headers",
            "login_max_length": "1",
            "login_min_length": "9",
            "login_special_char": "login_custom_special",
            "login_textarea_custom": " !@# ",
            "ratio": "",
            "records_no": "100",
            "same_form": "same_form",
            "txt": ""})
        form = SameForm()
        x = form.validate_on_submit()
        for fieldname, value in form.errors.items():
            assert 'ratio' in fieldname
            assert "This field is required." in value


def test_radio_required():
    with app.test_client() as c:
        c.post(data={
            "amount": "1-12",
            "headers": "y_headers",
            "login_max_length": "1",
            "login_min_length": "9",
            "login_special_char": "",
            "login_textarea_custom": " !@# ",
            "ratio": "80",
            "records_no": "100",
            "same_form": "same_form",
            "txt": ""})
        form = SameForm()
        x = form.validate_on_submit()
        for fieldname, value in form.errors.items():
            assert 'login_special_char' in fieldname
            assert "This field is required." in value