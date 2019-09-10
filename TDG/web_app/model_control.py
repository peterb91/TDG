"""
This module takes care of creating an instance of Flask app, defines routes to be resolved,
and takes care of processing web form data.
"""

from flask import request, Flask, app, redirect, render_template, url_for
import time
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from TDG.core.data_generation import generate_logins_and_passwords
from TDG.core.generate_output_file import _generate_output_name, _replace_boolean, _file_writer
from TDG.web_app.forms_login import LoginForm, RegisterForm
import os
from io import StringIO
from .forms_data_generation import SameForm, DifferentForm
from flask_wtf.csrf import CSRFProtect
from .database import init_db
from .database import FileHistory, User  # drop_tables, LoginHistory
from sqlalchemy.exc import IntegrityError


app._static_folder = os.path.abspath('static')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'DEV_ENV_KEY'
app.config['WTF_CSRF_ENABLED'] = True
database_type = 'sqlite'
database_name = 'login_test.db'
db_sessionmaker = init_db(database_type, database_name)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
csrf = CSRFProtect(app)
csrf.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_session = db_sessionmaker()
    return db_session.query(User).filter_by(user_id=user_id).first()


@app.route('/')
def toplevel():
    return redirect(url_for('index'))


@app.route('/index.html')
def index():
    """
    App route for index page.

    :return: rendered template.
    """
    return render_template('index.html', current_user=current_user)


@app.route('/same', methods=['POST', 'GET'])
def same():
    """
    App route for generating logins and passwords with the same constraints.

    :return: rendered template.
    """
    form = SameForm()
    return render_template('same.html', form=form)


@app.route('/history')
@login_required
def history():
    """
    App route for displaying user's history of generated files.

    :return: rendered template.
    """

    def all_constraints():
        user_id = current_user.user_id
        db_session = db_sessionmaker()
        var = list(db_session.query(FileHistory).filter_by(user_id=user_id))
        len_list = len(var)
        for item in var:
            item.created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(item.created_at))
        return var, len_list

    return render_template('history.html', value=all_constraints())


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    App route for signing in. After successful login, redirection to main page

    :return: rendered template.
    """
    db_session = db_sessionmaker()
    form = LoginForm()
    if form.validate_on_submit():
        user = db_session.query(User).filter_by(name=form.login.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login_error.html', form=form)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    """
    App route for signing up. After successful registration, redirection to login page

    :return: rendered template.
    """
    form = RegisterForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        db_session = db_sessionmaker()
        try:
            new_user = User(name=form.login.data, email=form.email.data, password=form.password.data)
            db_session.add(new_user)
            db_session.commit()
        except IntegrityError:
            return render_template('register_error.html', form=form)
        else:
            return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/different', methods=['POST', 'GET'])
def different():
    """
    App route for generating logins and passwords with different constraints.

    :return: rendered template.
    """
    form = DifferentForm()
    return render_template('different.html', form=form)


@app.route('/about')
def about():
    """
    App route for about section.

    :return: rendered template.
    """
    return render_template('about.html')


@app.route('/profile')
@login_required
def profile():
    """
    App route for user administration panel.

    :return: rendered template.
    """
    return render_template('profile.html', current_user=current_user)


@app.route('/406')
def invalid_input():
    """
    App route for handling invalid input data.

    :return: rendered template.
    """
    return render_template('406.html'), 406


def get_constraints_data(name):
    """
    This function processes request form for getting login or password data.

    :param name: login or password
    :return: dictionary with login or password data.
    """
    if name == 'login':
        return dict(login_or_password='login',
                    min_length=int(request.form['login_min_length']),
                    max_length=int(request.form['login_max_length']),
                    positive_percentage=int(request.form['ratio']),
                    list_length=int(request.form['records_no']))
    elif name == 'pass':
        return dict(min_length=int(request.form['pass_min_length']),
                    max_length=int(request.form['pass_max_length']))
    else:
        return 'wrong key'


def file_format():
    """
    This function returns file format.

    :return: a sting: 'txt' or 'csv'. In case of invalid input data, invalid_input() view is being rendered.
    """
    if 'txt' in request.form:
        return 'txt'
    elif 'csv' in request.form:
        return 'csv'
    else:
        return invalid_input()


def content_type():
    """
    This function returns file MIME type.

    :return: file MIME type. In case of invalid input data, invalid_input() view is being rendered.
    """
    if 'txt' in request.form:
        return 'text/plain;charset=utf-8'
    elif 'csv' in request.form:
        return 'text/csv;charset=utf-8'
    else:
        return invalid_input()


def special_characters(name):
    """
    This function prepares special characters string to be used during data generation.

    :param name: login or password
    :return: a string containing special characters, as determined in the form. In case of invalid input data,
        invalid_input() view is being rendered.
    """
    if name + '_all_special' in request.form.get(name + '_special_char'):
        return '`~!@#$%^&*()_+-=[]{}|\;\':\",<.>/?'
    elif name + '_none_special' in request.form.get(name + '_special_char'):
        return ''
    elif name + '_custom_special' in request.form.get(name + '_special_char'):
        return request.form.get(name + '_textarea_custom')
    else:
        return invalid_input()


def headers():
    """
    This function determines if headers should be generated in the output file.

    :return: True, False or invalid_input() view, in case of invalid input data.
    """
    if 'y_headers' in request.form.get('headers'):
        return True
    elif 'n_headers' in request.form.get('headers'):
        return False
    else:
        return invalid_input()


def create_dictionaries():
    """
    This function composes login and password dictionary. File format is determined using
    file_format() function, special characters are determined by calling special_characters()
    function. Additional get_constraints_data() and pass_data() functions are used to get form constraints
    for both logins and passwords.

    :return: dictionaries containing login and password constraints.
    """
    login_dictionary = get_constraints_data('login')
    login_dictionary['file_format'] = file_format()
    login_dictionary['characters'] = special_characters('login')
    login_dictionary['headers'] = headers()

    password_dictionary = dict(login_dictionary)
    password_dictionary['login_or_password'] = 'password'

    if 'pass_min_length' in request.form:
        password_dictionary.update(get_constraints_data('pass'))
        password_dictionary['characters'] = special_characters('pass')

    return login_dictionary, password_dictionary


def saving_file(name, constraints, output):
    """
    Function creates file in 'web_app/static/files' directory on server side.
    If user is not authenticated, file is not saved. If user is authenticated,
    opens session, and saves file information to database.

    :param name: name of file, generated based on current time
    :param constraints: dictionaries of constraints
    :param output: data generated by generate_logins_and_passwords function
    :return:
    """

    if current_user.is_authenticated:
        extension = file_format()
        header = 'yes' if headers() else 'no'
        db_session = db_sessionmaker()
        db_session.add(FileHistory(user_id=current_user.user_id,
                                   records_no=constraints[0]['list_length'],
                                   ratio=constraints[0]['positive_percentage'],
                                   headers=header,
                                   login_min_length=constraints[0]['min_length'],
                                   login_max_length=constraints[0]['max_length'],
                                   login_textarea_custom=constraints[0]['characters'],
                                   pass_min_length=constraints[1]['min_length'],
                                   pass_max_length=constraints[1]['max_length'],
                                   pass_textarea_custom=constraints[1]['characters'],
                                   file_path='files/%s' % name,
                                   file_extension=extension,
                                   created_at=time.time()))
        db_session.commit()
        db_session.close()
        with open('web_app/static/files/' + name, 'a', newline='') as file:
            _file_writer(file, extension, output, header)


@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    """
    App route for handling form data.

    :return: stream of generated logins and passwords with headers consisting of HTTP status 200,
        the MIME type of file determined by the content_type() function and filename determined by
        _generate_output_name() function.
    """

    if 'same_form' in request.form:
        form = SameForm()
        print('SAME found')
        form.validate_on_submit()
        print('POST request valid')
    elif 'different_form' in request.form:
        form = DifferentForm()
        print('DIFFERENT found')
        form.validate_on_submit()
        print('post request valid')

    constraints = create_dictionaries()
    extension = file_format()
    output = _replace_boolean(generate_logins_and_passwords(constraints))
    output_text = StringIO('')
    _file_writer(output_text, extension, output, headers())
    name = _generate_output_name(extension)
    saving_file(name, constraints, output)

    return output_text.getvalue(), 200, {
        'content-type': content_type(),
        'content-disposition': 'attachment; filename={}'.format(name),
    }
